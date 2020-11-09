from django import forms
from .models import Item, Container, Location, Room

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'image']
        
    
class AddContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name', 'image']


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
    

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room 
        fields = ['name']