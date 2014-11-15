from django.db import models

# Create your models here.
class Course(models.Model):
	fullName = models.CharField(max_length=200);
