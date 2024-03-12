from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} teaches {self.last_name}"
