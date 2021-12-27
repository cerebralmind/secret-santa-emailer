#!/usr/bin/env python
import os
import uuid

from box import Box
from PIL import Image, ImageDraw, ImageFont

def gen_image(giver, recipient, config):
    image_config = config.images
    im = Image.open('images/secret_santa.jpg')
    draw = ImageDraw.Draw(im)
    arialFont = ImageFont.truetype(image_config['font'], 42)
    draw.text((100, 150), f"Merry Christmas {giver}!", fill='black', font=arialFont)
    draw.text((100, 250), f"You are {recipient}'s", fill='green', font=arialFont)
    draw.text((100, 350), 'Secret Santa!', fill='red', font=arialFont)
    draw.text((250, 500), 'Ho! Ho! Ho!', fill='black', font=arialFont)
    file_name = '/tmp/%s.png' % giver
    im.save(file_name)
    return file_name

if __name__ == '__main__':
    names = ['Nicolas', 'Claus', 'Rudolph', 'Dasher', 'Donner', 'Vixen']
    config, credentials, images = {}, {}, {}

    images['font'] = 'RobotoSlab-VariableFont_wght.ttf'
    images['font_path'] = '/Users/devinv/Library/Fonts/'

    config['images'] = images

    config = Box(config)

    for name in names:
        file_name = gen_image(name, name, config)
        print(file_name)
