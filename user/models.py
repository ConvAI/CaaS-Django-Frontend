from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    c_name = models.CharField(max_length=120)
    c_desc = models.TextField(blank=True)
    c_type = models.CharField(max_length=100,default="None")
    c_url = models.URLField(blank=True)
    c_logo = models.ImageField(upload_to='c_logos',blank=True)
    
    def __str__(self):
        return self.user.username