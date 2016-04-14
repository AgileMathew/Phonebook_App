from django.db import models

# Create your models here.

class Data(models.Model):
	name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
