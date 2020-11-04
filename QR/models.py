from django.contrib.auth.models import User
from django.db import models

from items.models import Container

from segno import make_qr
from PIL import Image

class QRBlock(models.Model):
    image = models.ImageField(upload_to='./../media/uploads/qr', blank=True, null=True)
    qr_count_horizontal = models.IntegerField(default=6)
    qr_count_vertical = models.IntegerField(default=8) 
    scale = models.IntegerField(default=15)
    
    created_by = models.ForeignKey(User, related_name='qrblocks', on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    change_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs): 
        super(QRBlock, self).save(*args, **kwargs)
        qr_block = self.create_block()
 
    def concat_horizontal_image(self, original_image, new_image):
        h_img = Image.new('RGB', ((original_image.width + new_image.width), original_image.height))
        h_img.paste(original_image, (0,0))
        h_img.paste(new_image, (original_image.width, 0))        
        return h_img

    def concat_vertical_image(self, original_image, new_image):
        v_img = Image.new('RGB', (original_image.width, (original_image.height + new_image.height)))
        v_img.paste(original_image, (0,0))
        v_img.paste(new_image, (0, original_image.height))
        return v_img
    
    def new_qr(self):        
        first_qr = QR.objects.create(qr_block=self)
        first_qr.create_qr(self)        
        path = f'./media/uploads/qr/{first_qr.id}.png'
        return Image.open(path)        

    def create_horizontal_block(self):
        # Create first QR code and open
        original_qr_img = self.new_qr()            
        # Create next n QR images and concat to last group of images going horizontally
        for x in range(self.qr_count_horizontal-1):
            new_qr_img = self.new_qr()
            original_qr_img = self.concat_horizontal_image(original_image=original_qr_img, new_image=new_qr_img)
        #print('width:', original_qr_img.width)
        return original_qr_img

    def create_block(self):        
        original_qr_block = self.create_horizontal_block()
        for y in range(self.qr_count_vertical-1):
            new_horizontal_block = self.create_horizontal_block()
            original_qr_block = self.concat_vertical_image(original_image=original_qr_block, new_image = new_horizontal_block)
        
        path = f'./media/uploads/qr/qrblock_{self.id}.png'
        original_qr_block.save(path)
        self.image = f'./../media/uploads/qr/qrblock_{self.id}.png'
        super(QRBlock, self).save()

class QR(models.Model):
    image = models.ImageField(upload_to='./../media/uploads/qr', blank=True, null=True)
    container = models.ForeignKey(Container, related_name='containers', on_delete=models.DO_NOTHING, blank=True, null=True)
    qr_block = models.ForeignKey(QRBlock, related_name='qrblocks', on_delete=models.CASCADE, blank=True, null=True)
    
    created_by = models.ForeignKey(User, related_name='qr', on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    change_at = models.DateTimeField(auto_now=True, null=True)

    def create_qr(self, QRBlock):
        qr_code = make_qr(self.id)
        segno_path = f'./media/uploads/qr/{self.id}.png'
        qr_code.save(segno_path, scale=self.qr_block.scale)  
        self.image = f'./../media/uploads/qr/{self.id}.png'
        self.save()
        return qr_code

