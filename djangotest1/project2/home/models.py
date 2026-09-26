from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name 
class About(models.Model):
    s_name = models.CharField(max_length=100)
    s_phone = models.CharField(max_length=20)
    s_email = models.EmailField()    
