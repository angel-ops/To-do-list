#To Do List

#import django
 from django.db import models

 class Todo(models.Model):
     added_date = models.DateTimeField()
     text = models.CharField(max_legth = 200)
     
#load
#get to do items
#show to do items
