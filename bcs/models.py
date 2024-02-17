from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserGroup(models.Model):
    groupId = models.IntegerField()
    userId = models.IntegerField()
    relation = models.ForeignKey(Users, related_name='id_user', on_delete=models.CASCADE)
    # relation = models.IntegerField()


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


class Users(AbstractUser):
    # userName = models.CharField(max_length=45)
    userId = models.ForeignKey(UserGroup, related_name='id_user', on_delete=models.CASCADE)
    avatar = models.CharField(max_length=45, verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name="کد فعالسازی ایمیل")
    password = models.CharField(max_length=45)
    access = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()

