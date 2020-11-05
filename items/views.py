from django.shortcuts import get_object_or_404, render

from .models import Container, Location, Room

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