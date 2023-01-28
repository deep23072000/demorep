from django.db import models

class record(models.Model):
    faicon=models.CharField(max_length=50)
    heading=models.CharField(max_length=255)
    content=models.CharField(max_length=255)
    color=models.CharField(max_length=50)

class work(models.Model):
    image=models.CharField(max_length=255)
    heading=models.CharField(max_length=255)
    content=models.CharField(max_length=255)

class benifits(models.Model):
    image=models.CharField(max_length=255)
    title=models.CharField(max_length=255)


#contact form
class info(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    contact=models.CharField(max_length=255)
    query=models.CharField(max_length=255)


# Create your models here.
