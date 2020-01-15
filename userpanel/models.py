from django.db import models
from user.models import UserProfileInfo
from django.contrib.auth.models import User

# Create your models here.

class Bot(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    c_info = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    bot_name = models.CharField(max_length=30)
    bot_api = models.CharField(max_length=200)
    


