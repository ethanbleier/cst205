# Ethan's Collage
# Resources used: https://holypython.com/python-pil-tutorial/creating-photo-collages/
from PIL import Image, ImageDraw

collage = Image.new("RGBA", (1500,1500), color=(255,255,255,255))
lst = [7035, 7036, 7037, 7035, 7036, 7037, 7035, 7036, 7037]

c=0
for i in range(0,1500,500):
    for j in range(0,1500,500):
        file = "images/collage/IMG_"+str(lst[c])+".PNG" #/Users/ethanbleier/cst205/images/collage/IMG_____.PNG
        photo = Image.open(file).convert("RGBA")
        photo = photo.resize((500,500))        
        
        collage.paste(photo, (i,j))
        c+=1
collage.show()
collage.save("images/collage/NatexTeddy_collage.png")