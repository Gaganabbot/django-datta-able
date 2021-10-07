from django.db import models

# Create your models here.
class Skills(models.Model):
	input_text = models.CharField(max_length=200)
	
	def __str__(self):
		return self.input_text