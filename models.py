from django.db import models

class teacher(models.Model):
    #two fields - 1 name and 1 for teaching area
      Name = models.CharField(max_length=25)
      Area = models.CharField(max_length=30)
