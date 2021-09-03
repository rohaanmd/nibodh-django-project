from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class course(models.Model):
    course_id = models.AutoField
    name =  models.CharField(max_length=50)
    desc =  models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to="course\images",default="https://via.placeholder.com/500x500.png?text=Default")
    pub_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50,default="web" )
    def __str__(self):
        return self.name

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.CharField(max_length=50,default="")
    name =  models.CharField(max_length=50)
    desc =  models.CharField(max_length=500)
    phone = models.IntegerField()
    screenshot = models.ImageField(upload_to="contact\images",default="https://via.placeholder.com/500x500.png?text=Default")
    pub_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class order(models.Model):
    jsonCart = models.CharField(max_length=200)
    email = models.CharField(max_length=50,default="")
    first_name =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    isSameBillingAddress = models.BooleanField(default=False)
    last_name =  models.CharField(max_length=50)
    address =  models.CharField(max_length=200)
    zip = models.IntegerField()
    order_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.email