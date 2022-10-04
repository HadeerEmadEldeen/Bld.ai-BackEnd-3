from django.db import models

# Create your models here.



class File(models.Model):
  file = models.FileField(blank= True , null = False,  max_length = 10000000000000 )

  class Meta:
    db_table = "File"
  
  