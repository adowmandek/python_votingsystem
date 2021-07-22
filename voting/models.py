from django.db import models

# Create your models here.
class votingsystem(models.Model):
    Name=models.CharField(max_length=12)
    id_Number=models.CharField(max_length=10)
    country=models.CharField(max_length=8)
    total_voters=models.CharField(max_length=15)
    
