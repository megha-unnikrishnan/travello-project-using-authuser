from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    description=models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    description=models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
