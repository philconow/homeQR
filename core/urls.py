from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from core.views import frontpage, about, contact, signup


urlpatterns = [

    path('', frontpage, name='frontpage'),     
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),

]