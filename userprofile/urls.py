from django.urls import path

from userprofile.views import dashboard

urlpatterns = [

    path('dashboard/', dashboard, name='dashboard'),
    
]