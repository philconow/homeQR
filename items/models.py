from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField, TextField
from django.db.models import signals
from django.core.files import File
from django.utils.text import slugify
from io import BytesIO
from PIL import Image

# Create your models here.

class Room(models.Model):
    name = CharField(max_length=250)
    slug = SlugField(max_length=250, blank=True, null=True)    

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)
    
    #def get_absolute_url(self):
    #    return f'/{self.slug}/'

class Location(models.Model):
    name = CharField(max_length=250)
    slug = SlugField(max_length=250, blank=True, null=True)     
    room = models.ForeignKey(Room, related_name='locations', on_delete=models.CASCADE, default=1)
    
    class Meta:
        verbose_name_plural = 'Locations'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)
    
    #def get_absolute_url(self):
    #    return f'/{self.slug}/'

class Container(models.Model):
    name            = CharField(max_length=250)
    slug            = SlugField(max_length=250, blank=True, null=True)       
    location        = models.ForeignKey(Location, related_name='containers', on_delete=models.CASCADE, default=1)
    created_at      = DateTimeField(auto_now_add=True)
    deleted_at      = DateTimeField(blank=True, null=True)
    delete_reason   = TextField(max_length=500, blank=True)
    no_container    = BooleanField(default = False)
    
    image           = models.ImageField(upload_to='./../media/uploads/containers', blank=True, null=True)
    thumbnail       = models.ImageField(upload_to='./../media/uploads/containers', blank=True, null=True)

    
    class Meta:
        verbose_name_plural = 'Containers'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        self.slug = slugify(self.name)
        super(Container, self).save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    #def get_absolute_url(self):
    #    return f'/{self.slug}/'

class Item(models.Model):
    name        = CharField(max_length=250)
    slug        = SlugField(max_length=250, blank=True, null=True)
    container   = models.ForeignKey(Container, related_name='items', on_delete=models.CASCADE, default=1)
    created_at  = DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)