from PIL import Image
import glob

image = Image.open('img/i6.webp')
image = image.convert('RGB')
image.save('image.png', 'png')

