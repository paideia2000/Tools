from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.TextField()
    age = models.IntegerField(null=True, blank=True) 
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Users, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title