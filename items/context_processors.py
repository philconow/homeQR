from .models import Room

def menu_rooms(request):
     rooms = Room.objects.all().order_by("name")
    
     return {'menu_rooms': rooms}
