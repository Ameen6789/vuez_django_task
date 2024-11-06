from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
user_types=(
    ("admin","admin"),
    ("employee","employee")
    )
departments=(
    ("it","IT"),
    ("admin","Administration"),
    ("marketing","Marketing"),
    ("accounting","Accounting"),
    ("hr","HR")
)

class User(AbstractUser):
    user_type=models.CharField(choices=user_types,max_length=10,default="admin")

class Employee(models.Model):
    phone_number=models.BigIntegerField()
    address=models.TextField(max_length=1024)
    department=models.CharField(choices=departments,max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    


