from django.db import models

# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    def __str__(self):
        return self.name
        