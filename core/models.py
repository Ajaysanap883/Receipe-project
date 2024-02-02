from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
  name=models.CharField(max_length=50)  
  email=models.EmailField(max_length=100)
  image=models.ImageField(upload_to='media/')

  def __str__(self):
    return self.name
