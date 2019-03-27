from django.db import models

# userData Model


class userData(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    userName = models.CharField(max_length=20)
    DOB = models.DateField()
    contactNumber = models.CharField(max_length=10)
    password = models.CharField(max_length=20)


def __str__(self):
    return self.name
