from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    courseID = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    SUBJECTS = (
    ("ANTH", "Anthropology"),
    ("ART ", "Art"),
    ("BIOL", "Biology"),
    ("CHEM"," Chemistry"),
    ("LING", "Linguistic Cognitive Science"),
    ("CSCI", "Computer Science"),
    ("ENGR", "Engineering"),
    ("EA  ", "Environmental Analysis"),
    ("HIST", "History"),
    ("MATH", "Math"),
    ("PHIL", "Philosophy"),
    ("PHYS", "Physics"),
    ("PSYC", "Psychology"),
    ("RLST", "Religious Studies"))

    def avg_review(self):
       total = 0
       numReviews = 0
       for x in Review.objects.get(course__exact=self):
          total += x.rating
          numReviews += 1
       return total/numReviews

class Review(models.Model):
    author = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    course = models.ForeignKey(Course)
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

    def assignCourse(self, course):
        self.course = course
        self.save()



class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def addCourse(self, course):
       self.courses.add(course)
       self.save()
