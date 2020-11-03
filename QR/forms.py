from django import forms
from .models import QRBlock

class AddQRBlockForm(forms.ModelForm):
    class Meta:
        model = QRBlock
        fields = ['qr_count_horizontal', 'qr_count_vertical', 'scale']