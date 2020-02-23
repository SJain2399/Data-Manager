from django.db import models

# Create your models here.
class SearchField(models.Model):   
    kind = models.CharField(max_length=30)
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=30)
    createdTime = models.DateTimeField(null = False) 
    modifiedTime = models.DateTimeField(null = False) 
    mimeType = models.CharField(max_length=100)