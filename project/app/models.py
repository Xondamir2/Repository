from django.db import models

# Create your models here.

class Clas(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    price = models.IntegerField()
    clas = models.ManyToManyField(Clas)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name