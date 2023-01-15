from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class RUserdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=20, null=True)
    Email = models.EmailField(max_length=40)
    Phone_no = models.IntegerField()
    Role = models.CharField(max_length=15)
    Branch = models.CharField(max_length=30)
    Clg_Year = models.CharField(max_length=10, default=None)
    Password = models.CharField(max_length=10)
    CmfPassword = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Date = models.CharField(max_length=15, null=True)
    Branch = models.CharField(max_length=30, null=True)
    Subject = models.CharField(max_length=30, null=True)
    Type = models.CharField(max_length=15, null=True)
    Uploadfile = models.FileField(null=True)
    Desc = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.Subject
