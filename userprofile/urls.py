from django.urls import path

from userprofile.views import view_dashboard

urlpatterns = [

    path('dashboard/', view_dashboard, name='view_dashboard'),
    
]