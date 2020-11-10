from django.urls import path

from items.views import (room_list, room_detail, location_detail, container_detail, item_detail,  
                        add_room, add_location, add_container, add_item,
                        delete_room, delete_location, delete_container, delete_item)

urlpatterns = [

    # Add pages    
    path('rooms/add-room/', add_room, name='add_room'),
    path('<slug:slug>/add-location/', add_location, name='add_location'),
    path('<slug:room_slug>/<slug:slug>/add-container/', add_container, name='add_container'),
    path('<slug:room_slug>/<slug:location_slug>/<slug:slug>/add-items/', add_item, name='add_item'),    
    
    # Delete Pages
    path('<slug:slug>/delete/', delete_room, name='delete_room'), 
    path('<slug:room_slug>/<slug:slug>/delete/', delete_location, name='delete_location'), 
    path('<slug:room_slug>/<slug:location_slug>/<slug:slug>/delete/', delete_container, name='delete_container'),
    path('<slug:room_slug>/<slug:location_slug>/<slug:container_slug>/<slug:slug>/delete/', delete_item, name='delete_item'),
    
    # Detail Pages
    path('rooms/', room_list, name='room_list'),
    path('<slug:slug>/', room_detail, name='room_detail'),     
    path('<slug:room_slug>/<slug:slug>/', location_detail, name='location_detail'),  
    path('<slug:room_slug>/<slug:location_slug>/<slug:slug>/', container_detail, name='container_detail'),    
    path('<slug:room_slug>/<slug:location_slug>/<slug:container_slug>/<slug:slug>/', item_detail, name='item_detail'),   

]