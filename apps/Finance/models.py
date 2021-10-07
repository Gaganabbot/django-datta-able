from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os


STATUS_CHOICES =(
    ("New", "New"),
    ("Incomplete", "Incomplete"),
    ("In Process", "In Process"),
	("Complete", "Complete"),
)
SUBJECT_CHOICES=(
	("Finance", "Finance"),
    ("Admin", "Admin"),
    ("Development", "Development"),
    ("Testing", "Testing"),
	("Audit", "Audit"),
    ("IT", "IT"),
	)
class Work(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100,blank=True)
	subject = models.CharField(choices = SUBJECT_CHOICES, max_length=100,blank=True)
	status = models.CharField(choices = STATUS_CHOICES, max_length=100,blank=True)
	estimate_time=models.IntegerField(blank=True,default=0)
	created_date = models.DateTimeField(blank=True,auto_now_add=True)
	updated_date = models.DateTimeField(blank=True,auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
