
from PIL import Image
from colorama import Fore, Back, Style
#from pathlib import Path

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

def get_pixel_matrix(img, height):
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def get_intensity_matrix(img, height):
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    brightness = [0.21 * r + 0.72 * g + 0.07 * b for r, g, b in pixels]
    #brightness = [(r + g +b) / 3.0 for r, g, b in pixels]
    #brightness = [(max(pixel) + min(pixel)) / 2.0 for pixel in pixels]
    return [brightness[i:i+img.width] for i in range(0, len(brightness), img.width)]

def convert_to_ascii(intensity_matrix, ascii_chars):
    ascii_matrix = []
    for row in intensity_matrix:
        ascii_row = []
        for p in row:
            ascii_row.append(ascii_chars[int(p/MAX_PIXEL_VALUE * len(ascii_chars)) - 1])
        ascii_matrix.append(ascii_row)

    return ascii_matrix

def invert_intensity_matrix(intensity_matrix):
    inverted_intensity_matrix = []
    for row in intensity_matrix:
        inverted_row = []
        for p in row:
            inverted_row.append(MAX_PIXEL_VALUE - p)
        inverted_intensity_matrix.append(inverted_row)

    return inverted_intensity_matrix

def print_ascii_matrix(ascii_matrix, text_color):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        print(text_color + "".join(line))
        #print(Back.WHITE + "".join(line))

    print(Style.RESET_ALL)


#cwd = Path.cwd()
img_path = "direct.jpg"
img = Image.open(img_path)

print(img.format, img.size, img.mode)

pixels_matrix = get_pixel_matrix(img, 100)
intensity_matrix = get_intensity_matrix(img, 100)
ascii_matrix = convert_to_ascii(intensity_matrix, ASCII_CHARS)
print_ascii_matrix(ascii_matrix, Fore.GREEN)

#print(pixels)