from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def dashboard(request):
    qrblocks = request.user.qrblocks.all()
    context = {
        'userprofile': request.user.userprofile,
        'qrblocks': qrblocks
    }
    return render(request, 'dashboard.html', context)
