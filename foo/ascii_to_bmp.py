# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

ASCII_MAP = {
    '.': (192, 192, 192),  # road
    '#': (0, 0, 0),  # wall
    # Vegetation:
    '(': (0, 128, 0),  # forest
    ')': (128, 128, 255),  # jungle
    '-': (0, 255, 128),  # plains
    '\'': (0, 128, 128),  # swamp
    # Wastes:
    '^': (128, 128, 128),  # mountain
    # '': (),  # volcano
    'u': (128, 64, 0),  # hills
    'v': (255, 0, 0),  # mountain pass
    '_': (255, 255, 255),  # tundra
    '=': (255, 255, 0),  # desert
    '"': (255, 128, 0),  # beach
    ';': (128, 128, 0),  # desolation
    # Water:
    '+': (0, 0, 255),  # sea
    '`': (0, 255, 255),  # lake
    '~': (0, 128, 255),  # river
    # '-': (0, 255, 255),  # brook
    # Special locations:
    '@': (128, 0, 128),
    '*': (255, 0, 255)  # cave
}
LOCATIONS = ['O', 'o',
             'a', 'b', 'c', 'd', 'e', 'f', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6',
             '!', '|', '%', '&', '$']
IGNORE = [' ', '\n']

# TODO: Name your map here:
MAP_NAME = "omega_world"


##################################################
# ASCII to Bitmap converter
##################################################
def convert_ascii():
    # Create a new image
    img = Image.new('RGB',
                    (100, 100),  # size
                    'white')  # background
    pxl = img.load()

    with open(f'maps_ascii/{MAP_NAME}.txt', 'r') as f:
        for ndx_l, l in enumerate(f.readlines()):
            for ndx_r, r in enumerate(l):
                if r in IGNORE:
                    continue
                elif r in LOCATIONS:
                    clr = ASCII_MAP['@']
                else:
                    clr = ASCII_MAP[r]

                pxl[ndx_r, ndx_l] = clr

    # for i in range(img.size[0]):
    #     for j in range(img.size[1]):
    #         pxl[i, j] = (0, 0, 255)

    img.save(f'maps_bmp/{MAP_NAME}.bmp')
    img.show()


if __name__ == "__main__":
    convert_ascii()
