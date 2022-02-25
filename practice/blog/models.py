from django.db import models
import uuid
# Create your models here.

class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length = 100,null = True)
    phone_number = models.CharField(max_length=500)
    about_me = models.CharField(max_length=500)
    address= models.CharField(max_length = 1000,null = True)
    city = models.CharField(max_length = 500,null = True)
    state = models.CharField(max_length = 500,null = True)
    country = models.CharField(max_length = 500,null = True)
    email = models.CharField(max_length = 500,null = True) 
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    
    
    class Meta:
        db_table = 'user_profile'