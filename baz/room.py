# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# import argparse
from random import randrange, randint

WIDTH = 20
HEIGHT = 20

currentMap = [['.' for y in range(HEIGHT)]
                for x in range(WIDTH)]
ROOMS = []

"""
psr = argparse.ArgumentParser(description="something something")
psr.add_argument('-a', action='store_true', help="help 1")
psr.add_argument('-b', action='store_true', help="help 2")
psr.add_argument('-c', '--cwc', help="help 3")
psr.add_argument('-v', '--version', action='version', version='0.1')
psr.add_argument('foo', action='extend', nargs='+')

args = psr.parse_args()
print(args.foo)
"""


def on_map(x, y):
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def in_room(x, y):
    for room in ROOMS:
        if room.x1 <= x <= room.x2 and room.y1 <= y <= room.y2:
            return True
    return False


def make_river(orientation=None):
    last_move = 0
    options = ['vertical', 'horizontal', 'diagonal']

    if orientation is None:
        orientation = options[randrange(3)]
    if orientation not in options:
        raise ValueError

    if orientation == 'horizontal':
        x = randint(1, WIDTH-2)
        y = 0
        while on_map(x, y):
            currentMap[x][y] = '~'
            if on_map(x + 1, y):
                currentMap[x+1][y] = '~'
            move = [last_move, 0, -1, -1, +1, +1]
            last_move = move[randrange(len(move))]
            x += last_move
            y += 1
            if on_map(x, y) and currentMap[x][y] == '~':
                break

    elif orientation == 'vertical':
        x = 0
        y = randint(1, HEIGHT-2)
        while on_map(x, y):
            currentMap[x][y] = '~'
            if on_map(x, y+1):
                currentMap[x][y+1] = '~'
            move = [last_move, 0, -1, -1, +1, +1]
            last_move = move[randrange(len(move))]
            y += last_move
            x += 1
            if on_map(x, y) and currentMap[x][y] == '~':
                break

    elif orientation == 'diagonal':
        x = 0
        y = 0
        while on_map(x, y):
            currentMap[x][y] = '~'
            if on_map(x+1, y):
                currentMap[x+1][y] = '~'
            if on_map(x, y+1):
                currentMap[x][y+1] = '~'
            move = [last_move, 0, -1, +1, +1]
            last_move = move[randrange(len(move))]
            if randrange(2):
                y += last_move
                x += 1
            else:
                x += last_move
                y += 1


class Room(object):
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.width = width
        self.height = height
        self.CenterX = (self.x1 + self.x2) / 2
        self.CenterY = (self.y1 + self.y2) / 2

    def intersects(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    def create_square_room(self):
        for x in range(self.x1 + 1, self.x2):
            for y in range(self.y1 + 1, self.y2):
                if on_map(x,y):
                    currentMap[x][y] = '.'


def make_rooms():
    for i in range(10):
        width = randrange(3,8)
        height = randrange(3, 8)
        x = randrange(1, WIDTH-2)
        y = randrange(1, HEIGHT-2)

        new_room = Room(x, y, width, height)
        failed = False
        for OtherRoom in ROOMS:
            if new_room.intersects(OtherRoom):
                failed = True
                break
        if failed:
            continue

        new_room.create_square_room()
        ROOMS.append(new_room)


if __name__ == "__main__":
    make_rooms()
    make_river()
    make_river()
    for x in range(WIDTH):
        print("".join(currentMap[x]))
    stuff = []
    for i in range(20):
        buc = 0
        while randrange(100) < 10:
            buc += 1
        while randrange(100) < 15:
            buc -= 1
        stuff.append(buc)

    print(stuff)
