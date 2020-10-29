from django.shortcuts import render, get_object_or_404
from .models import QR


# Create your views here.

# def get_qr_all(request, id):
#     qr = get_object_or_404(QR, id=id)
#     context = {
#         'qr': qr,
#     }
    
#     return render(request, 'qr_list.html', context)

def qr_list(request):
    return render(request, 'qr_list.html')