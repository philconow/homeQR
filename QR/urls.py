from django.urls import path

from QR.views import add_qr_block, view_qr_block, delete_qr_block, view_qr_code, scan_qr_code

urlpatterns = [

    # QR Block pages
    path('block/add/', add_qr_block, name='add_qr_block'),   
    path('block/view/<int:qrblock_id>/', view_qr_block, name='view_qr_block'),
    path('block/delete/<int:qrblock_id>/', delete_qr_block, name='delete_qr_block'),

    # QR Code pages
    path('code/view/<int:qr_id>/', view_qr_code, name='view_qr_code'),
    path('code/scan/', scan_qr_code, name='scan_qr_code'),

]