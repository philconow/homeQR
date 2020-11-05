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
from userprofile.views import dashboard
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

from core.views import frontpage, about, contact, signup
from items.views import container_detail, location_detail, room_detail, room_list
from QR.views import add_qr_block, view_qr_block, delete_qr_block, view_qr_code
from userprofile.views import dashboard

urlpatterns = [
    path('', frontpage, name='frontpage'),  
    path('admin/', admin.site.urls),    
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),

    path('qr/block/add/', add_qr_block, name='add_qr_block'),   
    path('qr/block/view/<int:qrblock_id>/', view_qr_block, name='view_qr_block'),
    path('qr/block/delete/<int:qrblock_id>/', delete_qr_block, name='delete_qr_block'),
    path('qr/code/view/<int:qr_id>/', view_qr_code, name='view_qr_code'),
    
    path('rooms/', room_list, name='room_list'),
    path('<slug:slug>/', room_detail, name='room_detail'), 
    path('<slug:room_slug>/<slug:slug>/', location_detail, name='location_detail'),  
    path('<slug:room_slug>/<slug:location_slug>/<slug:slug>/', container_detail, name='container_detail'),    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
