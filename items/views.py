from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Container, Location, Room
from .forms import AddItemForm, AddContainerForm, AddLocationForm, AddRoomForm

def container_detail(request, room_slug, location_slug, slug):
    container = get_object_or_404(Container, slug=slug)
    context = { 
        'container': container        
    }

    return render(request, 'container_detail.html', context)

def location_detail(request, room_slug, slug):
    location = get_object_or_404(Location, slug=slug)
    containers = location.containers.all()
    context = {
        'location': location,
        'containers': containers
    }

    return render(request, 'location_detail.html', context)

def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    locations = room.locations.all()
    context = {
        'room': room,
        'locations': locations
    }
    return render(request, 'room_detail.html', context)

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required
def add_room(request):
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            qr_block = form.save(commit=False)
            qr_block.created_by = request.user         
            qr_block.save()            
            return redirect('room_list')
    else:
        form = AddRoomForm()    
    return render(request, 'add_room.html', {'form': form})

@login_required
def add_location(request):
    if request.method == 'POST':
        form = AddLocationForm(request.POST)
        if form.is_valid():
            qr_block = form.save(commit=False)
            qr_block.created_by = request.user         
            qr_block.save()            
            return redirect('room_list') # TODO: change redirect link
    else:
        form = AddLocationForm()    
    return render(request, 'add_location.html', {'form': form})

@login_required
def add_container(request):
    if request.method == 'POST':
        form = AddContainerForm(request.POST)
        if form.is_valid():
            qr_block = form.save(commit=False)
            qr_block.created_by = request.user         
            qr_block.save()            
            return redirect('room_list') # TODO: change redirect link
    else:
        form = AddContainerForm()    
    return render(request, 'add_container.html', {'form': form})



@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            qr_block = form.save(commit=False)
            qr_block.created_by = request.user         
            qr_block.save()            
            return redirect('room_list') # TODO: change redirect link
    else:
        form = AddItemForm()    
    return render(request, 'add_item.html', {'form': form})


