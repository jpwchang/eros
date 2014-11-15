from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_length=10000)
    RATING_CHOICES = (
    (0.0, "0"),
    (0.5, "0.5"),
    (1.0, "1"),
    (1.5, "1.5"),
    (2.0, "2"),
    (2.5, "2.5"),
    (3.0, "3"),
    (3.5, "3.5"),
    (4.0, "4"),
    (4.5, "4.5"),
    (5.0, "5"))
    rating = models.FloatField(choices=RATING_CHOICES)

class Course(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    review = models.ForeignKey(Review)

class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    course = models.ForeignKey(Course)



