from django.db import models

# Create your models here.

class Hobby(models.Model):
    hobby_name = models.CharField()
    hobby_desc = models.TextField()


    def __str__(self):
        return self.hobby_name
    


