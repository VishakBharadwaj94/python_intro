#resize our files

from PIL import Image
import os 

size_300 = (300,300)

for f in os.listdir('.'):
	if f.endswith('.png'):
		image = Image.open(f)
		name,ext = os.path.splitext(f)
		image.thumbnail(size_300)
		image.save(f'resized/{name}.{ext}')