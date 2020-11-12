from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Item, Container, Location, Room
from .forms import AddItemForm, AddContainerForm, AddLocationForm, AddRoomForm

def item_detail(request, room_slug, location_slug, container_slug, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'items/item_detail.html', {'item':item})

def container_detail(request, room_slug, location_slug, slug):
    container = get_object_or_404(Container, slug=slug)
    items = container.items.all()
    context = {
        'container': container,
        'items': items
    }
    return render(request, 'items/container_detail.html', context)

def location_detail(request, room_slug, slug):
    location = get_object_or_404(Location, slug=slug)
    containers = location.containers.all()
    context = {
        'location': location,
        'containers': containers
    }
    return render(request, 'items/location_detail.html', context)

def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    locations = room.locations.all()
    context = {
        'room': room,
        'locations': locations
    }
    return render(request, 'items/room_detail.html', context)

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'items/room_list.html', {'rooms': rooms})

@login_required
def add_room(request):
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_by = request.user         
            room.save()            
            return redirect('room_list')
    else:
        form = AddRoomForm()    
    return render(request, 'items/add_room.html', {'form': form})


@login_required
def add_location(request, slug):
    room = get_object_or_404(Room, slug=slug)
    if request.method == 'POST':
        form = AddLocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.created_by = request.user
            location.room = room
            location.save()            
            return redirect('room_list') # TODO: change redirect link
    else:
        form = AddLocationForm()  
    return render(request, 'items/add_location.html', {'room':room, 'form':form})


@login_required
def add_container(request, room_slug, slug):
    location = get_object_or_404(Location, slug=slug)
    if request.method == 'POST':        
        form = AddContainerForm(request.POST, files=request.FILES)
        if form.is_valid():
            container = form.save(commit=False)
            container.created_by = request.user
            container.location = location         
            container.save()            
            return redirect('room_list') # TODO: change redirect link
    else:
        form = AddContainerForm()    
    return render(request, 'items/add_container.html', {'location':location, 'form':form})


@login_required
def add_item(request, room_slug, location_slug, slug):
    container = get_object_or_404(Container, slug=slug)
    if request.method == 'POST':
        form = AddItemForm(request.POST, files=request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.container = container           
            item.save()            
            return redirect('room_list') # TODO: change redirect link
    else:
        form = AddItemForm()    
    return render(request, 'items/add_item.html', {'container':container, 'form':form})


@login_required
def delete_room(request, slug):
    if request.user.is_superuser:
        room = get_object_or_404(Room, slug=slug)
    else:
        room = get_object_or_404(Room, slug=slug, created_by=request.user)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')         
    return render(request, 'items/delete_room.html', {'room': room})


@login_required
def delete_location(request, room_slug, slug):
    if request.user.is_superuser:
        location = get_object_or_404(Location, slug=slug)
    else:
        location = get_object_or_404(Location, slug=slug, created_by=request.user)
    if request.method == 'POST':
        location.delete()
        return redirect('room_list') # TODO: Possibly change         
    return render(request, 'items/delete_location.html', {'location': location})


@login_required
def delete_container(request, room_slug, location_slug, slug):
    if request.user.is_superuser:
        container = get_object_or_404(Container, slug=slug)
    else:
        container = get_object_or_404(Container, slug=slug, created_by=request.user)
    if request.method == 'POST':
        container.delete()
        return redirect('room_list') # TODO: Possibly change         
    return render(request, 'items/delete_container.html', {'container': container})


@login_required
def delete_item(request, room_slug, location_slug, container_slug, slug):
    if request.user.is_superuser:
        item = get_object_or_404(Item, slug=slug)
    else:
        item = get_object_or_404(Item, slug=slug, created_by=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('room_list') # TODO: Possibly change         
    return render(request, 'items/delete_item.html', {'item': item})