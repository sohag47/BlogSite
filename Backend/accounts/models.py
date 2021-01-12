from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ExtraUserInfo(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(null=True, blank=True, upload_to='userimage/')
    country = models.CharField(max_length=250, null=True, blank=True)
    language = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_info
