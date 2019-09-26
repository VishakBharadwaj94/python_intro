from PIL import Image,ImageFilter


image = Image.open('lenna.png')
# image.rotate(90).save('lenna_right.png')
# image.filter(ImageFilter.GaussianBlur()).save('lenna_blur.png')