from django.db import models


# Create your models here.
class DemoEmployee(models.Model):
     name = models.CharField( max_length=120)
     Emailid = models.EmailField(default=None,)
     password = models.CharField(default=None,max_length=120)
     confirmpassword = models.CharField(default=None,max_length=120)
    
     class Meta:
        db_table= "Customer"
