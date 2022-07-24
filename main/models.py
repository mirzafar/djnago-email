from django.db import models


class Email(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.email


class User(models.Model):
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    login = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return self.first_name
