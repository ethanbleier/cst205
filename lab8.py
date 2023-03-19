from PIL import Image
img = Image.open('images/mona4k.jpg')
#print(dir(img))
size = (45, 45)
img.thumbnail(size, reducing_gap=3.0)
img.show()


#this method, thumbnail, is cool because it creates a thumbnail with preserved aspect ratio of the original
# a downside of this method is it alters your original image. luckily, i dont care.
#the method calculates an appropriate thumbnail size to preserve the aspect ratio of the image


#Line 484
#This class represents an image object.  To create
#:py:class:`~PIL.Image.Image` objects, use the appropriate factory
#functions.  There's hardly ever any reason to call the Image constructor
# directly.
#* :py:func:`~PIL.Image.open`
# * :py:func:`~PIL.Image.new`
#* :py:func:`~PIL.Image.frombytes`