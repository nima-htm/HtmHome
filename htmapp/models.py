from django.db import models

# Create your models here.
class information(models.Model):
    infoPlace= models.CharField(max_length=20)
    infoText= models.CharField(max_length=100000)
    
class portfolio(models.Model):
    Name = models.CharField(max_length=40)