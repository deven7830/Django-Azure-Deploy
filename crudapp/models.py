from django.db import models

# Create your models here.
class Tanishq(models.Model):
    cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=90)
    choice=models.CharField(max_length=90)
    paymentMode=models.CharField(max_length=90)
    image = models.ImageField(upload_to='media')
    date=models.DateField()
    email=models.EmailField()
