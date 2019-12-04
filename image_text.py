#!/usr/bin/env python
import os
import uuid

from box import Box
from PIL import Image, ImageDraw, ImageFont

def gen_image(giver, recipient, config):
    image_config = config.images
    im = Image.open('images/secret_santa.png')
    draw = ImageDraw.Draw(im)
    fontsFolder = image_config['font_path']
    arialFont_small = ImageFont.truetype(image_config['font'], 24)
    arialFont = ImageFont.truetype(image_config['font'], 42)
    draw.text((75, 350), f"{recipient}'s", fill='green', font=arialFont)
    draw.text((540, 350), 'Secret Santa', fill='red', font=arialFont)
    file_name = '/tmp/%s.png' % giver
    im.save(file_name)
    return file_name

if __name__ == '__main__':
    names = ['Nicolas', 'Claus', 'Rudolph', 'Dasher', 'Donner', 'Vixen']
    config, credentials, images = {}, {}, {}

    images['font'] = 'RobotoSlab-VariableFont:wght.ttf'
    images['font_path'] = '/Users/devin.vitone/Library/Fonts/'

    config['images'] = images

    config = Box(config)

    for name in names:
        file_name = gen_image(name, name, config)
        print(file_name)
