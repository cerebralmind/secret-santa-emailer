#!/usr/bin/env python2.7
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

def gen_image(giver, recipient, config):
    image_config = config.images
    im = Image.open('images/secret_santa.png')
    draw = ImageDraw.Draw(im)
    fontsFolder = image_config['font_path']
    arialFont_small = ImageFont.truetype(image_config['font'], 24)
    arialFont = ImageFont.truetype(image_config['font'], 48)
    draw.text((100, 25), 'Hello %s,' % giver, fill='white', font=arialFont_small)
    draw.text((250, 170), 'of', fill='white', font=arialFont)
    draw.text((430, 100), recipient, fill='gray', font=arialFont)
    file_name = '/tmp/%s.png' % giver
    im.save(file_name)
    return file_name

if __name__ == '__main__':
    names = ['Nicolas', 'Claus', 'Rudolph', 'Dasher', 'Donner', 'Vixen']
    for name in names:
        file_name = gen_image(name, name)
        print(file_name)
