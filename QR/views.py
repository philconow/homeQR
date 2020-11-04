from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from QR.models import QRBlock

from .forms import AddQRBlockForm

def qr_block_list(request):
    qrblocks = QRBlock.objects.all()
    return render(request, 'qr_block_list.html', {'qrblocks', qrblocks})

@login_required
def add_qr_block(request):
    if request.method == 'POST':
        form = AddQRBlockForm(request.POST)
        if form.is_valid():
            qr_block = form.save(commit=False)
            qr_block.created_by = request.user
            qr_block.save()
            return redirect('dashboard.html')
    else:
        form = AddQRBlockForm()
    
    return render(request, 'add_QRBlock.html', {'form': form})