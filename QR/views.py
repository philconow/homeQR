from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from QR.models import QRBlock, QR

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
    return render(request, 'QR/add_qr_block.html', {'form': form})

@login_required
def view_qr_block(request, qrblock_id):
    if request.user.is_superuser:
        qrblock = get_object_or_404(QRBlock, pk=qrblock_id)
    else:
        qrblock = get_object_or_404(QRBlock, pk=qrblock_id, created_by=request.user)
    qrs = qrblock.qrs.all()
    context = {
        'qrblock': qrblock,
        'qrs': qrs
    }
    return render(request, 'QR/view_qr_block.html', context)

@login_required
def delete_qr_block(request, qrblock_id):
    if request.user.is_superuser:
        qrblock = get_object_or_404(QRBlock, pk=qrblock_id)
    else:
        qrblock = get_object_or_404(QRBlock, pk=qrblock_id, created_by=request.user)
    if request.method == 'POST':
        qrblock.delete()
        return redirect('dashboard')         
    return render(request, 'QR/delete_qr_block.html', {'qrblock': qrblock})

@login_required
def view_qr_code(request, qr_id):
    if request.user.is_superuser: 
        qr = get_object_or_404(QR, pk=qr_id)
    else:
        qr = get_object_or_404(QR, pk=qr_id, created_by=request.user)
    return render(request, 'QR/view_qr_code.html', {'qr': qr})

# TODO: Fix this view
def scan_qr_code(request):
    return render(request, 'QR/scan.html')




