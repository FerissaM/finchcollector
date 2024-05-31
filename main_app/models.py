from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    meal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.finch.name} fed {self.meal}"