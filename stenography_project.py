from PIL import Image
import numpy as np
from pyfiglet import Figlet
import pyfiglet

def hide_image():
    cover_path = input("Enter the path to the cover image: ")
    secret_path = input("Enter the path to the secret image: ")
    bits = int(input("Enter the hide bit: "))
    cover_image = Image.open(cover_path).convert('RGBA')
    secret_image = Image.open(secret_path).convert('RGBA')
    cover_data = np.array(cover_image)
    secret_data = np.array(secret_image)
    do_hide_image(cover_data, secret_data, bits)
    hidden_image = Image.fromarray(cover_data, 'RGBA')
    hidden_image.save("hidden_image.png")
    print("Hidden image saved as 'hidden_image.png'")

def do_hide_image(cover_data, secret_data, bits):
    min_w = min(cover_data.shape[1], secret_data.shape[1])
    min_h = min(cover_data.shape[0], secret_data.shape[0])
    mask = (0xFF >> bits) << bits
    for y in range(min_h):
        for x in range(min_w):
            # Red
            cover_data[y, x, 0] = (cover_data[y, x, 0] & mask) + (secret_data[y, x, 0] >> (8 - bits))
            # Green
            cover_data[y, x, 1] = (cover_data[y, x, 1] & mask) + (secret_data[y, x, 1] >> (8 - bits))
            # Blue
            cover_data[y, x, 2] = (cover_data[y, x, 2] & mask) + (secret_data[y, x, 2] >> (8 - bits))

def unhide_image():
    steg_path = input("Enter the path to the steganographic image: ")
    bits = int(input("Enter the number of bits used for hiding: "))
    steg_image = Image.open(steg_path).convert('RGBA')
    steg_data = np.array(steg_image)
    do_unhide_image(steg_data, bits)
    revealed_image = Image.fromarray(steg_data, 'RGBA')
    revealed_image.save("revealed_secret.png")
    print("Revealed secret image saved as 'revealed_secret.png'")

def do_unhide_image(steg_data, bits):
    h, w, _ = steg_data.shape

    for y in range(h):
        for x in range(w):
            # Red
            steg_data[y, x, 0] = (steg_data[y, x, 0] << (8 - bits)) & 0xFF
            # Green
            steg_data[y, x, 1] = (steg_data[y, x, 1] << (8 - bits)) & 0xFF
            # Blue
            steg_data[y, x, 2] = (steg_data[y, x, 2] << (8 - bits)) & 0xFF

print("***********************************************************************************************")
f = pyfiglet.figlet_format("Stenography Image - Image", font="slant")
print(f)
print("***********************************************************************************************")
choose = input("Enter 1 for hide:\nEnter 2 for unide: ")
if choose == '1':
    hide_image()
elif choose == '2':
    unhide_image()
else:
    print("Invaild input:")
    exit()
print("***********************************************************************************************")