from django.db import models
# from datetime import datetime, date




# Create your models here.
class User(models.Model):
    # firstname=models.CharField(max_length=30)
    # lastname=models.CharField(max_length=30)
    firstname=models.CharField(blank=True, null=True,max_length=30)
    Surname=models.CharField(blank=True, null=True,max_length=20)
    gender = (("M","Male"),("F","Female"),)
    gender = models.CharField(blank=True, null=True, max_length=50)

    birthdate = models.CharField(blank=True, null=True, max_length=50)
    relation =  models.CharField(blank=True, null=True, max_length=50)                           


class registration(models.Model):
    username = models.CharField(blank=True, null=True,max_length=30)

    password = models.CharField(blank=True, null=True,max_length=20)
    first_name = models.CharField(blank=True, null=True,max_length=30)
    last_name = models.CharField(blank=True, null=True,max_length=30)

	# firstname=models.CharField(blank=True, null=True,max_length=30)








class loggedin(models.Model):
    username = models.CharField(blank=True, null=True,max_length=30)

    password = models.CharField(blank=True, null=True,max_length=20)
	
	# firstname=models.CharField(blank=True, null=True,max_length=30)


















