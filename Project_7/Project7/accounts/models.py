from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class More_User_Details(models.Model):
    relation = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    hobby = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(blank=True, upload_to='profile_pics', default='profile_pics/blank-avatar.png')

