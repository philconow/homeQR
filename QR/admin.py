from django.contrib import admin

from .models import QR, QRBlock

# Register your models here.
admin.site.register(QR)
admin.site.register(QRBlock)