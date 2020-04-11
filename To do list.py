#To Do List
from django.db import models

class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_legth = 200)

#no se que hace xDDDDDDD
#load
#get to do items
#show to do items

#add other to do list
#delate to do list