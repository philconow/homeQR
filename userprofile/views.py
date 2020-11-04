from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from userprofile.models import User
from QR.models import QRBlock

@login_required
def dashboard(request):
    qrblocks = request.user.qrblocks.all()
    context = {
        'userprofile': request.user.userprofile,
        'qrblocks': qrblocks
    }
    return render(request, 'dashboard.html', context)

@login_required
def view_qrblock(request, qrblock_id):
    qrblock = get_object_or_404(QRBlock, pk=qrblock_id, created_by=request.user)
    return render(request, 'view_qrblock.html', {'qrblock': qrblock})
