from PIL import Image

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_pixel_matrix(img, height):
    img.thumbnail((height, 175))        # resize image to new dimensions
    pixel_matrix = list(img.getdata())  # 
    pixel_matrix = [pixel_matrix[i:i+img.width] for i in range(0, len(pixel_matrix), img.width)]

    return pixel_matrix

def get_brightness_matrix(pixel_matrix):
    brightness_matrix = []
    
    for row in pixel_matrix:
        brightness_row = []

        for pixel in row:
            brightness = (pixel[0] + pixel[1] + pixel[2]) / 3
            brightness_row.append(brightness)
        
        brightness_matrix.append(brightness_row)

    return brightness_matrix

def get_ascii_matrix(brightness_matrix):
    ''' brightness ranges from 0-255
        must map brightness 0-255 to characters 0-64
        --> (((brightness / 255) * 65) - 1)
    '''
    ascii_matrix = []
    
    for row in brightness_matrix:
        ascii_row = []

        for brightness in row:
            ascii_val = ASCII_CHARS[int(((brightness / 255) * 65) - 1)]
            ascii_row.append(ascii_val)
        
        ascii_matrix.append(ascii_row)

    return ascii_matrix

img = Image.open("sample-eye.jpg")

pixel_matrix = get_pixel_matrix(img, 800)
brightness_matrix = get_brightness_matrix(pixel_matrix)
ascii_matrix = get_ascii_matrix(brightness_matrix)

for row in ascii_matrix:
    line = [p+p+p for p in row]
    print("".join(line))