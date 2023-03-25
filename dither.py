from PIL import Image

obr = Image.open("kitt.jpg")
from PIL import Image

def find_closest_pallete_color(oldpixel):
    return (round (oldpixel[0]/255)*255), (round (oldpixel[1]/255)*255), (round (oldpixel[2]/255)*255)

def twoTuplesMinus(t1, t2):
    return t1[0]-t2[0],t1[1]-t2[1],t1[2]-t2[2]

def twoTuplesPlus(t1, t2, const):
    return (int(t1[0]+t2[0]*const), int(t1[1]+t2[1]*const), int(t1[2]+t2[2]*const))

pixels = obr.load()

for y in range(obr.size[1]-1):
    for x in range(1,obr.size[0]-1):
        oldpixel = pixels[x,y]
        newpixel = find_closest_pallete_color(oldpixel)
        pixels[x,y] = newpixel
        quant_error = twoTuplesMinus (oldpixel, pixels[x, y])
        pixels [x + 1, y] = twoTuplesPlus (pixels[x + 1, y], quant_error, 7 / 16)
        pixels [x - 1, y + 1] = twoTuplesPlus (pixels[x - 1, y + 1], quant_error, 3/16)
        pixels [x , y + 1] = twoTuplesPlus (pixels[x, y + 1], quant_error, 5/16)
        pixels [x + 1, y + 1] = twoTuplesPlus (pixels[x + 1, y + 1], quant_error, 1/16)

obr.show()







