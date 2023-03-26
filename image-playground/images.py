from PIL import Image, ImageFilter

img = Image.open('./Pokedex/199 pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("grey.png",'png')
#png allows image filters