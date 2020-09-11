from django.db import models

# Create your models here.
class Talking(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
