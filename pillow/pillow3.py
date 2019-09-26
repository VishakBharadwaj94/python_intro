from PIL import Image
import os 

for f in os.listdir('.'):
	if f.endswith('.png'):
		image = Image.open(f)
		name,ext = os.path.splitext(f)
		image.save(f'pmgs/{name}.png')
		
