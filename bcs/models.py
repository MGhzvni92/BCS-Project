from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_to(instance, filename):
    return 'uploads/images/cow/{}_{}'.format(instance.code, filename)


class Cow(models.Model):
    code = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=upload_to, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - title: {self.title}"


class BcsData(models.Model):
    cow = models.ForeignKey(Cow, to_field='code', on_delete=models.CASCADE)
    score = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cow.code} - Score: {self.score} - Date: {self.create_date.strftime('%Y-%m-%d')}"

