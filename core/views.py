from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from items.models import Container

def frontpage(request):
    containers = Container.objects.all()
    return render(request, 'core/frontpage.html', {'containers': containers})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Logs in and authenticates user
            return redirect('view_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})