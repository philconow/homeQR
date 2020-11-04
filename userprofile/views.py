from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from QR.models import QRBlock

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def view_qrblock(request, qrblock_id):
    qrblock = get_object_or_404(QRBlock, pk=qrblock_id, created_by=request.user)
    return render(request, 'view_qrblock.html', {'qrblock': qrblock})
