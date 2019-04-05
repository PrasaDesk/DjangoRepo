from django.db import models

# userData Model


class userData(models.Model):
    firstname = models.CharField(max_length=20, default='')
    lastname = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=30, default='',
                             unique=True, null=False)
    username = models.CharField(max_length=20, default='', unique=True)
    gender = models.CharField(max_length=6, default='')
    dob = models.DateField()
    contactno = models.CharField(max_length=10, default='')
    password = models.CharField(max_length=20, default='')
    security_question = models.CharField(default='', max_length=50)
    security_answer = models.CharField(default='', max_length=20)


def __str__(self):
    return self.name
