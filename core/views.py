from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from items.models import Container

# Create your views here.

def frontpage(request):
    containers = Container.objects.all()
    context = {
        'containers': containers
    }

    return render(request, 'frontpage.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) # Logs in and authenticates user
            return redirect('dashboard')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})