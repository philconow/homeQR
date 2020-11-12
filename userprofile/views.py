from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from QR.models import QRBlock

@login_required
def view_dashboard(request):
    if request.user.is_superuser:
        qrblocks = QRBlock.objects.all()
    else:
        qrblocks = request.user.qrblocks.all()
    context = {
        'userprofile': request.user.userprofile,
        'qrblocks': qrblocks
    }
    return render(request, 'userprofile/dashboard.html', context)
    