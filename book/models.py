from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete =  models.CASCADE)
    