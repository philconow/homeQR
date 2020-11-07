from django import forms

from .models import Item, Container, Location, Room

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'container']
    
class AddContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name', 'location', 'no_container']

class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'room']

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room 
        fields = ['name']