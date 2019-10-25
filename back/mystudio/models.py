from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.CharField(max_length=250,default="")
    create_time=models.DateTimeField('date published')
    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    def __str__(self):
        return self.first_name+" "+self.last_name
