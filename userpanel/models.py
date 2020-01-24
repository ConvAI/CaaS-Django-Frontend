from django.db import models
from user.models import UserProfileInfo
from django.contrib.auth.models import User

# Create your models here.
lang_names = {'en-us':'English-US','en-uk':'English-UK'}



class Language(models.Model):
    lang_code = models.CharField(max_length=10)
    lang_name = models.CharField(max_length=50)

class Bot(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    c_info = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    bot_name = models.CharField(max_length=30)
    bot_api = models.CharField(max_length=150,null=True,blank=True)
    enabled = models.BooleanField(default=True)
    bot_desc = models.CharField(max_length=300,null=True,blank=True)
    paragraph = models.CharField(max_length=150,null=True,blank=True)
    metapath = models.CharField(max_length=150,null=True,blank=True)
    storagelink = models.CharField(max_length=200,null=True,blank=True)
    lang = models.ForeignKey(Language,on_delete=models.DO_NOTHING)




