from django.db import models
from django.contrib.auth.models import User


class User_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='')
    dob = models.DateField(default='')
    contactno = models.CharField(max_length=10, default='')
    sequrity_que = models.CharField(max_length=100, default='')
    sequrity_ans = models.CharField(max_length=100, default='')

    def __str__(self):
        return "{0} ---> {1}".format(self.user.id, self.user.username)
