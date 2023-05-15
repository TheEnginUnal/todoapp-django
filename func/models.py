
from django.contrib.auth.models import User
from django.db import models
from datetime import date
class ToDoList(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    creationDate = models.DateField(default=date.today)
    updateDate = models.DateField(null=True,blank=True)
    deletionDate = models.DateField(null=True, blank=True)
    completion = models.DecimalField(default=0, max_digits=5,decimal_places=2)

class ToDoItem(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    listid = models.ForeignKey("func.ToDolist",  on_delete=models.CASCADE)
    creationDate = models.DateField(default=date.today)
    updateDate = models.DateField(null=True,blank=True)
    deletionDate = models.DateField(null=True, blank=True)
    content = models.TextField(max_length=250)
    completion = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    

