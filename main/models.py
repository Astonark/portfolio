from django.db import models


# Create your models here.
class Competences(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField


class Tags(models.Model):
    name = models.CharField(max_length=280)


class Project(models.Model):
    name = models.CharField(max_length=280)


class Presentation(models.Model):
    description = models.CharField(max_length=560)

    def __str__(self):
        return self.description
