"""homeQR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import frontpage, about, contact
from items.views import container_detail, location_detail, room_detail
from QR.views import qr_list

urlpatterns = [
    path('', frontpage, name='frontpage'),  
    path('admin/', admin.site.urls),    
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('qr/', qr_list, name='qr_list'),

    path('<slug:slug>/', room_detail, name='room_detail'), 
    path('<slug:room_slug>/<slug:slug>/', location_detail, name='location_detail'),  
    path('<slug:room_slug>/<slug:location_slug>/<slug:slug>/', container_detail, name='container_detail'),    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
