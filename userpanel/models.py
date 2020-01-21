from django.db import models
from user.models import UserProfileInfo
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
    lang_code = models.CharField(max_length=10)
    lang_name = models.CharField(max_length=50)

class Bot(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    c_info = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    bot_name = models.CharField(max_length=30)
    bot_api = models.CharField(max_length=150)
    enabled = models.BooleanField()
    bot_desc = models.CharField(max_length=300)
    metapath = models.CharField(max_length=150)
    storagelink = models.CharField(max_length=200)
    lang = models.ForeignKey(Language,on_delete=models.DO_NOTHING)



