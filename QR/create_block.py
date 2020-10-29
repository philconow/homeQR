from segno import make_qr
from PIL import Image

# Dimensions of QR codes on A4 Page 
qr_count_horizontal = 5
qr_count_vertical = 8

def create_qr(id):
    qr_code = make_qr(id)
    qr_code.save(f'./media/uploads/qr/{id}.png', scale=15)
    return qr_code


def concat_horizontal_image(original_image, new_image):
    # Create Dimensions for new background image
    background_image = Image.new('RGB', ((original_image.width + new_image.width), original_image.height))
    # Paste original image into background
    background_image.paste(original_image, (0,0))
    # Paste new image into background 
    background_image.paste(new_image, (original_image.width, 0))
    
    return background_image

def concat_vertical_image(original_image, new_image):
    # Create Dimensions for new background image
    background_image = Image.new('RGB', (original_image.width, (original_image.height + new_image.height)))
    # Paste original image into background
    background_image.paste(original_image, (0,0))
    # Paste new image into background 
    background_image.paste(new_image, (0, original_image.height))
    
    return background_image

def create_horizontal_qr_block(start_id):
    # Create first QR code and open
    create_qr(start_id)
    original_qr_img = Image.open(f'./media/uploads/qr/{start_id}.png')
        
    # Create next 4 QR images and concat to last group of images going horizontally
    for qr_id in range(start_id + 1, start_id + qr_count_horizontal):
        create_qr(qr_id)
        new_qr_img = Image.open(f'./media/uploads/qr/{qr_id}.png')
        original_qr_img = concat_horizontal_image(original_qr_img, new_qr_img)
    print('width:', original_qr_img.width)
    return original_qr_img



start_id = 1 
original_qr_block = create_horizontal_qr_block(start_id)

# Loop to create to create new horizontal blocks and paste vertically
for qr_id in range(start_id, qr_count_vertical):
    new_horizontal_block = create_horizontal_qr_block(start_id + (qr_id * qr_count_horizontal))
    original_qr_block = concat_vertical_image(original_qr_block, new_horizontal_block)

qr_directory = f'./media/uploads/qr/'
block_file_name = f'{qr_directory}/qrblock_{start_id}-{start_id+(qr_count_horizontal*qr_count_vertical-1)}.png'
original_qr_block.save(block_file_name)