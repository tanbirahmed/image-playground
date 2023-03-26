from PIL import Image, ImageFilter

img = Image.open('./201 astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')