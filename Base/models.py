from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.TimeField(auto_now=True)
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    # user = 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  
    description = models.TextField
    updated = models.TimeField(auto_now=True)
    created = models.TimeField(auto_now_add=True)
    