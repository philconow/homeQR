from django.db import models
from django.core.files import File
from items.models import Container

from segno import make_qr
from PIL import Image

# Create your models here.

class QRBlock(models.Model):
    image = models.ImageField(upload_to='./media/uploads/qr/', blank=True, null=True)
    qr_count_horizontal = models.IntegerField(default=5)
    qr_count_vertical = models.IntegerField(default=8) 
    start_block = models.IntegerField(blank=True, null=True)
    end_block = models.IntegerField(blank=True, null=True)


    # def get_qr_index():
    #     return QR.objects.latest('id') + 1
    def save(self, *args, **kwargs):
        super(QRBlock, self).save(*args, **kwargs)
        qr_block = self.create_block()
        qr_directory = f'./media/uploads/qr/'
        block_full_path = f'{qr_directory}qrblock_{self.id}.png'        
        qr_block.save(block_full_path)
        saved_img = open(block_full_path, 'rb')
        self.image.save(block_full_path, File(saved_img), save=False)        
        super(QRBlock, self).save(*args, **kwargs)
 
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
        first_qr = QR()
        first_qr.save()
        first_qr.create_qr(self)        
        path = f'./media/uploads/qr/{first_qr.id}.png'
        return Image.open(path)
         

    def create_horizontal_block(self):
        # Create first QR code and open
        original_qr_img = self.new_qr()            
        # Create next n QR images and concat to last group of images going horizontally
        for x in range(self.qr_count_horizontal):
            new_qr_img = self.new_qr()
            original_qr_img = self.concat_horizontal_image(original_image=original_qr_img, new_image=new_qr_img)
        #print('width:', original_qr_img.width)
        return original_qr_img

    def create_block(self):        
        original_qr_block = self.create_horizontal_block()
        for y in range(self.qr_count_vertical):
            new_horizontal_block = self.create_horizontal_block()
            original_qr_block = self.concat_vertical_image(original_image=original_qr_block, new_image = new_horizontal_block)
        return original_qr_block



class QR(models.Model):
    image = models.ImageField(upload_to='./media/uploads/qr/', blank=True, null=True)
    container = models.ForeignKey(Container, related_name='containers', on_delete=models.DO_NOTHING, blank=True, null=True)
    qr_block = models.ForeignKey(QRBlock, related_name='qrblocks', on_delete=models.CASCADE, blank=True, null=True)
    scale = models.IntegerField(default=15)
    
    def create_qr(self, QRBlock):
        qr_code = make_qr(self.id)
        path = f'./media/uploads/qr/{self.id}.png'
        qr_code.save(path, scale=self.scale)        
        saved_img = open(path, 'rb')
        self.image.save(f'./media/uploads/qr/{self.id}.png', File(saved_img), save=False)
        self.qr_block.save(QRBlock)
        return qr_code

