from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

# Create your models here.


class Bmi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.bmi
# class DietRecommend(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     weight = models.FloatField()
#     height = models.FloatField()
#     bmi = models.FloatField()
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.bmi