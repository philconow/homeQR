from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from QR.models import QRBlock

from .forms import AddQRBlockForm

@login_required
def add_qr_block(request):
    if request.method == 'POST':
        form = AddQRBlockForm(request.POST)
        if form.is_valid():
            qr_block = form.save(commit=False)
            qr_block.created_by = request.user         
            qr_block.save()            
            return redirect('dashboard')
    else:
        form = AddQRBlockForm()    
    return render(request, 'add_qr_block.html', {'form': form})