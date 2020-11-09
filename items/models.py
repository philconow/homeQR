from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField, TextField
from django.core.files import File
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from io import BytesIO
from PIL import Image



class Room(models.Model):
    name = CharField(max_length=250)
    slug = SlugField(max_length=250, blank=True, null=True)    
    
    created_by = models.ForeignKey(User, related_name='rooms', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    change_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)
    
class Location(models.Model):
    name = CharField(max_length=250)
    slug = SlugField(max_length=250, blank=True, null=True)     
    room = models.ForeignKey(Room, related_name='locations', on_delete=models.CASCADE)
    
    created_by = models.ForeignKey(User, related_name='locations', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    change_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Locations'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)
    
class Container(models.Model):
    name            = CharField(max_length=250)
    slug            = SlugField(max_length=250, blank=True, null=True)       
    location        = models.ForeignKey(Location, related_name='containers', on_delete=models.CASCADE)
    deleted_at      = DateTimeField(blank=True, null=True)
    delete_reason   = TextField(max_length=500, blank=True)
    
    image           = models.ImageField(upload_to='./../media/uploads/containers', blank=True, null=True)
    
    created_by      = models.ForeignKey(User, related_name='containers', on_delete=models.SET_NULL, null=True)
    created_at      = models.DateTimeField(auto_now_add=True, null=True)
    change_at       = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Containers'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Container, self).save(*args, **kwargs)

class Item(models.Model):
    name        = CharField(max_length=250)
    slug        = SlugField(max_length=250, blank=True, null=True)
    container   = models.ForeignKey(Container, related_name='items', on_delete=models.CASCADE)
    created_at  = DateTimeField(auto_now_add=True)
    
    image       = models.ImageField(upload_to='./../media/uploads/items', blank=True, null=True)
    
    created_by  = models.ForeignKey(User, related_name='items', on_delete=models.SET_NULL, null=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True)
    change_at   = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)