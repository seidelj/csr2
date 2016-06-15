from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import random

def get_now():
    return timezone.now()
# Create your models here.

class Mturker(models.Model):
    user = models.OneToOneField(User)
    treatment = models.CharField(max_length=256, null=True)
    verified = models.IntegerField(default=0)
    accepted = models.IntegerField(null=True)
    start = models.DateTimeField(null=True, blank=True)
    batch = models.CharField(max_length=256)

    def get_task(self):
        images = Images.filter(batch=self.batch)
        tasks = self.user.task_set.all()
        unfinished = tasks.filter(status=0)
        remaining = len(images)-len(tasks)
        if len(unfinished)>0:
            print "Number of unfinished tasks:",len(unfinished)
            current = unfinished[0]
        elif len(unfinished) == 0:
            for x in range(len(images)):
                tempImage = random.choice(images)
                current, created = Task.get_or_create(user_id=self.user.id, image_id=tempImage.id)
                if created == True:
                    break
                else:
                    current = False
        if not current:
            entry = False
        else:
            entry = "text" if current.readable else "readable"
        return current, entry



class Image(models.Model):
    filename = models.CharField('Filename', max_length=512)
    batch = models.CharField(max_length=256)

    def get_url(self):
        return "http://bfidata.s3-website-us-east-1.amazonaws.com/libraryimages/{}".format(self.filename)

    def check_status(self,user):
        rs = user.task_set.filter(task_id=self.id)
        if rs.count() == 1:
            status = rs[0].finished
        else:
            status = 0
        return status

    def __str__(self):
        return self.filename

class WorkTimer(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey("Task", null=True)
    page = models.CharField(max_length=28, null=True)
    value = models.IntegerField()
    token = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

class Task(models.Model):

    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)

    readable = models.IntegerField(null=True)
    text = models.TextField(null=True, blank=True)
    order = models.IntegerField(null=True)
    status = models.IntegerField(default=0)

    timestarted = models.DateTimeField(default=get_now)
    timefinished = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == 1 and self.timefinished == None:
            self.timefinished = get_now()
        super(Task, self).save(*args, **kwargs)

def get_now():
    return timezone.now()

class EventLog(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task, null=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True)
    timestamp = models.DateTimeField(default=get_now)



