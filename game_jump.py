import pygame as pg
import random
import math

pg.init()

display_width = 600
display_height = 400

gameDisplay = pg.display.set_mode((display_width,display_height))

pg.display.set_caption("aryamaan chutiya")

def distance(cord1, cord2):
    return ((cord1[0]-cord2[0])*2+(cord1[1]-cord2[1])2)*0.5

def collide(img, img1, x, y, x1, y1):
    player_mask = pg.mask.from_surface(img)
    obj_mask = pg.mask.from_surface(img1)

    offset = (int(x1-x), int(y1-round(y)))

    col_point = player_mask.overlap(obj_mask, offset)

    if col_point:
        return True
    return False

def sign(x):
    try:
        return round(x/abs(x))
    except ZeroDivisionError:
        return 0

def num_print(win, score, x, y, col=(255, 255, 255), b_col=(0, 0, 0)):
    number = []
    if score == 0:
        number.append(0)
    else:
        while score > 0:
            number.append(score % 10)
            score //= 10
    i = (len(number)-1)
    while i >= 0:
        img = color_chng(digit[number[i]], (255, 255, 255), col)
        img = color_chng(img, (20, 24, 28), b_col)
        win.blit(img, (x, y))
        x += 27
        i -= 1
    return x

def color_chng(img, col1, col2):

    image_pixel_array = pg.PixelArray(img.convert_alpha())
    image_pixel_array.replace(col1, col2)
    img = pg.PixelArray.make_surface(image_pixel_array)

    return img

digit = [pg.image.load('images/digit/0.png'), pg.image.load('images/digit/1.png'),
         pg.image.load('images/digit/2.png'), pg.image.load('images/digit/3.png'),
         pg.image.load('images/digit/4.png'), pg.image.load('images/digit/5.png'),
         pg.image.load('images/digit/6.png'), pg.image.load('images/digit/7.png'),
         pg.image.load('images/digit/8.png'), pg.image.load('images/digit/9.png')]

