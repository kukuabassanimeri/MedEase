from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.fullname
    
class BookQueue(models.Model):
    Fullname = models.CharField(max_length=255)
    Phonenumber = models.CharField(max_length=30)
    Email = models.EmailField()
    Message = models.TextField()
    IsPending = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Fullname