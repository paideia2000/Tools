from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.TextField()
    age =  age = models.IntegerField(null=True, blank=True) 
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tittle