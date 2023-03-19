from PIL import Image

im1 = Image.open('hw2_images/AdWLrEX9jK.png').convert('RGBA')
im2 = Image.open('hw2_images/bpoQ3CCQME.png').convert('RGBA')


im3 = Image.composite(im1, im2, mask)

im3.show()

