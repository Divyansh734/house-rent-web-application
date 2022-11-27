from django.db import models

# Create your models here.
class Post(models.Model):
 photo = models.ImageField(upload_to="myimage")

 title = models.CharField(max_length=150)
 rent=models.IntegerField()
 date = models.DateField(auto_now_add=True)
 desc = models.TextField()

class Contact(models.Model):
 name = models.CharField(max_length=150)
 email = models.EmailField(max_length=150)
 address = models.CharField(max_length=500)
 message = models.TextField()
