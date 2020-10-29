from django.shortcuts import render

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