from django.contrib.auth.models import AbstractUser
from django.db import models

class Cow(models.Model):
    cowName = models.CharField(max_length=45)
    groupId = models.IntegerField()


class CowGroup(models.Model):
    type = models.IntegerField()
    cowLandId = models.IntegerField()
    cowGroupName = models.CharField(max_length=45)


class CowLand(models.Model):
    cowLandName = models.CharField(max_length=45)


class CowLandUser(models.Model):
    cowLandId = models.IntegerField()
    userId = models.IntegerField()
    relation = models.IntegerField()


class CowState(models.Model):
    cowId = models.IntegerField()
    dateTime = models.DateTimeField()
    cowState = models.IntegerField()
    description = models.CharField(max_length=5000)


class StateGroup(models.Model):
    groupId = models.IntegerField()
    dateTime = models.DateTimeField()
    groupState = models.IntegerField()
    description = models.CharField(max_length=5000)


class InputData(models.Model):
    dateTime = models.DateTimeField()
    type = models.IntegerField()
    sourceAddress = models.CharField(max_length=300)
    cowId = models.IntegerField()
    userId = models.IntegerField()


class Notification(models.Model):
    dateTime = models.DateTimeField()
    content = models.CharField(max_length=500)


class UserNotification(models.Model):
    userId = models.IntegerField()
    notificationId = models.IntegerField()
    state = models.IntegerField()
