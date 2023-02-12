from django.db import models


class ngo(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)
    password= models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class phil(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)
    password= models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=30)
    mission = models.CharField(max_length=500)
    history =  models.CharField(max_length=500)
    impact =  models.CharField(max_length=500)
    image =  models.ImageField(upload_to='images')

    def _str_(self):  
        return self.caption

class Contact(models.Model):
    name= models.CharField(max_length=125)
    email=models.EmailField(max_length=150)
    number= models.IntegerField()
    message=models.CharField(max_length =400)
    # datetime=models.DateField()
    

   
    def _str_(self):
        return self.name 