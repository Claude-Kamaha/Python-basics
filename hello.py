# blur an image
from PIL import Image,ImageFilter

before = Image.open("flower.bmp")
after = before.filter(ImageFilter.BLUR)
after.save("out.bmp")