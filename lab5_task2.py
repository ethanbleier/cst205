#sunset filter
from PIL import Image
im2 = Image.open('images/beach.jpg')

negative_list = [(p[0], int(.5*p[1]), int(.5*p[2]))
                            for p in im2.getdata()]

im2.putdata(negative_list)
im2.show()