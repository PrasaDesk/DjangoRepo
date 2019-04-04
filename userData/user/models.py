from django.db import models
from django.contrib.auth.models import User


class User_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    bio = models.CharField(max_length=100, default='')
    sequrity_que = models.CharField(max_length=100, default='')
    sequrity_ans = models.CharField(max_length=100, default='')

    def __str__(self):
        return "{0} ---> {1} {2}".format(self.user.username, self.user.first_name, self.user.last_name)
