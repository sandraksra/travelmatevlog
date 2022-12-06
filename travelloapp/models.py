from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class Testimonia(models.Model):
    pic=models.ImageField(upload_to='pic1')
    day=models.IntegerField()
    month=models.TextField()
