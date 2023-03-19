from PIL import Image

im = Image.open('images/beautiful_4k.jpg')

#luminance method
grayscale = [((p[0]*299 + p[1]*587 + p[2]*114 )//1000,) * 3
                            for p in im.getdata()]

im.putdata(grayscale)
im.show(grayscale)