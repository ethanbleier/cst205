#Monica Is The Goat
#imports pillow
from PIL import Image 

#reads file
with open("txt files/monalisa.txt", "r") as f: 
    line_list = f.readlines()

#assigns width and height from file info
mona_width = len(line_list[0].split())
mona_height = len(line_list)

#'paints' new pillow image
mona = Image.new('L', (mona_width, mona_height))

#  loops below iterate thru monalisa.txt 
#  && paints pixels on each coord

for counter, line_element in enumerate(line_list):
    for counter2, l in enumerate(line_element.split()):
        mona.putpixel((counter2, counter), int(l))

#this was a bitch to figure out
new_mona = mona.transpose(Image.ROTATE_270)
new_mona.show("new_mona.jpg")
new_mona.save("images/new_mona.jpg")