from PIL import Image

#open file, read only
with open('txt files/cb.txt', 'r') as f:
    line_list = f.readlines()

#assigns x && y
img_w = len(line_list[0].split())
img_h = len(line_list)

#makes new image
img = Image.new('RGB', (img_w, img_h))

#this is where stuff gets done
for c, line_element in enumerate(line_list):
    for c2, t in enumerate(line_element.split()):
        img.putpixel((c2, c), eval(t))

#oh my lord this took way too long to get right
new_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
new_img = new_img.transpose(Image.Transpose.ROTATE_90)


new_img.save('images/new_img.jpg')
new_img.show('new_img.jpg')