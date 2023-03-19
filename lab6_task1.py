from PIL import Image

im = Image.open('images/beautiful_4k.jpg')

#avg method
grayscale = [((p[0] + p[1] + p[2])//3,)*3
                            for p in im.getdata()]

im.putdata(grayscale)
im.show(grayscale)