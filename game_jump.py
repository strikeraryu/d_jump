import pygame as pg
import random
import math

pg.init()

display_width = 600
display_height = 400
jump_vel = 40
crate_vel = 30
g = 10
max_crate = 3
obj_y = 300
score = 0

digit = [pg.image.load('images/digit/0.png'), pg.image.load('images/digit/1.png'),
         pg.image.load('images/digit/2.png'), pg.image.load('images/digit/3.png'),
         pg.image.load('images/digit/4.png'), pg.image.load('images/digit/5.png'),
         pg.image.load('images/digit/6.png'), pg.image.load('images/digit/7.png'),
         pg.image.load('images/digit/8.png'), pg.image.load('images/digit/9.png')]

plant_jump = [pg.image.load('images/plant_jump/plant_jump (1).png'),
              pg.image.load('images/plant_jump/plant_jump (2).png'),
              pg.image.load('images/plant_jump/plant_jump (3).png'),
              pg.image.load('images/plant_jump/plant_jump (4).png')]
plant_jump = [pg.transform.scale(img, (64, 68)) for img in plant_jump]
plant_run = [pg.image.load('images/plant_run/plant_run (1).png'), pg.image.load('images/plant_run/plant_run (2).png'),
             pg.image.load('images/plant_run/plant_run (3).png'), pg.image.load('images/plant_run/plant_run (4).png')]
plant_run = [pg.transform.scale(img, (64, 68)) for img in plant_run]

crate_img = pg.image.load('images/crate.png')
crate_img = pg.transform.scale(crate_img, (40, 45))
chest_img = pg.image.load('images/chest.png')
chest_img = pg.transform.scale(chest_img, (40, 45))
stone_img = pg.image.load('images/stone.png')
stone_img = pg.transform.scale(stone_img, (40, 45))

base_img = pg.image.load('images/base.jpeg')

win = pg.display.set_mode((display_width, display_height))
pg.display.set_caption("aryamaan chutiya running")
clock = pg.time.Clock()


def distance(cord1, cord2):
    return ((cord1[0] - cord2[0]) ** 2 + (cord1[1] - cord2[1]) ** 2) ** 0.5


def collide(img, img1, x, y, x1, y1):
    player_mask = pg.mask.from_surface(img)
    obj_mask = pg.mask.from_surface(img1)

    offset = (int(x1 - x), int(y1 - round(y)))

    col_point = player_mask.overlap(obj_mask, offset)

    if col_point:
        return True
    return False


def sign(x):
    try:
        return round(x / abs(x))
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
    i = (len(number) - 1)
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


# ------------------------

class plant(object):
    img = plant_run[0]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wlk_cnt = 0
        self.jump = False
        self.vel_y = 0

    def move(self):
        if self.jump == True:
            self.y -= self.vel_y
            self.vel_y -= g
            if self.vel_y < -jump_vel:
                self.jump = False
                self.jump_vel = 0

    def draw(self):
        if not self.jump:
            self.img = plant_run[self.wlk_cnt]
            win.blit(self.img, (self.x, self.y))
            self.wlk_cnt += 1
            if self.wlk_cnt >= 4: self.wlk_cnt = 0
        else:
            self.img = plant_run[0]
            win.blit(self.img, (self.x, self.y))
            self.wlk_cnt = 0


class crate_obj(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def move(self):
        self.x -= crate_vel

    def draw(self):
        win.blit(self.img, (self.x, self.y))


def redrawgamewindow():
    win.fill((0, 0, 0))

    for b in base:
        b.draw()

    plant.draw()
    for crate in crates:
        crate.draw()

    num_print(win, score, 300, 30)
    pg.display.update()


run = True
plant = plant(100, obj_y)
crates = []
base = []
base.append(crate_obj(0, 300, base_img))

while run:
    clock.tick(14)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    keys = pg.key.get_pressed()

    if keys[pg.K_UP] and not plant.jump:
        plant.jump = True
        plant.vel_y = jump_vel

    if len(crates) <= max_crate:

        temp_img = random.choice([chest_img, stone_img, crate_img])

        if len(crates) != 0:
            new_crate = crate_obj(crates[-1].x + random.randint(300, 400), obj_y + 20, temp_img)
            crates.append(new_crate)
        if len(crates) == 0:
            new_crate = crate_obj(700, obj_y + 20, temp_img)
            crates.append(new_crate)

    if len(base) <= max_crate:
        new_base = crate_obj(base[-1].x + 336, 300, base_img)
        base.append(new_base)

    for crate in crates:
        if crate.x < 0:
            crates.pop(crates.index(crate))
            score += 1
            crate_vel += 0.5
        if collide(plant.img, crate_img, plant.x, plant.y, crate.x, crate.y):
            quit()
        crate.move()

    for b in base:
        if b.x < -336:
            base.pop(base.index(b))
        b.move()
    plant.move()

    redrawgamewindow()