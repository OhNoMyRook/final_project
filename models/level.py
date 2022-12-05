import pygame as pg
import json

pg.init()

WHITE = (200, 200, 200)
CYAN = (0, 150, 150)
BLACK = (0, 0, 0)
BROWN = (100, 50, 20)

def scale_objects(objects, scales):
    '''Скейлит объекты под разрешение экрана пользователя'''
    scale_x, scale_y = scales

    for object in objects:
        object.x *= scale_x
        object.xx *= scale_x
        object.y *= scale_y
        object.yy *= scale_y

class Platform:
    '''Конструктор класса Platform
    Args:
    screen -
    x - 
    y - 
    xx - 
    yy -
    '''
    def __init__(self, screen, x, y, xx, yy):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.color = BLACK
        self.screen = screen

    def draw(self):
        '''Рисует платформы на уровне'''
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.xx, self.yy))

    def move(self):
        '''Движение платформ при прохождении'''
        self.x -= 0.1


class Spike:
    '''Конструктор класса Spike
    Args:
    screen - 
    x -
    y -
    color -
    '''
    def __init__(self, screen, x, y, a, color=CYAN):
        self.x = x
        self.y = y
        self.xx = 25
        self.yy = 25
        self.screen = screen
        self.color = color

    def draw(self):
        '''Рисует шипы на уровне'''
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.xx, self.yy))

    def move(self):
        '''Движение шипов при прохождении'''
        self.x -= 0.1

def read_data(screen, platforms, spikes, input_file):
    '''Считывает данные о расположении платформ и шипов с файла input_file'''
    with open(input_file, 'r') as file:
        data = json.load(file)
        count_of_platforms = len(data[0]['platform'])
        for i in range(count_of_platforms):
            platform = Platform(screen, **data[0]['platform'][i])
            platforms.append(platform)
        count_of_spikes = len(data[1]['spike'])
        for i in range(count_of_spikes):
            spike = Spike(screen, **data[1]['spike'][i])
            spikes.append(spike)

def check_passage():
    '''Проверяет прохождение уровня'''
    #FIXME: Условие при котором уровень будет пройден return True
    return False

class Game:
    '''Конструктор класса Game
    Args:
    screen - экран
    platforms - список платформ
    spikes - список шипов
    '''

    def __init__(self, screen, platforms, spikes, func):
        self.screen = screen
        self.platforms = platforms
        self.spikes = spikes
        self.func = func
       
    def init_game(self):
        '''Запуск игры'''
        self.func = True
        pg.display.update()
        finished = False
        while not finished:
            self.screen.fill(WHITE)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True

            for platform in self.platforms:
                platform.draw()
            for spike in self.spikes:
                spike.draw()
            
            if check_passage():
                #FIXME: когда уровень пройден нужно открыть дверь
                for el in self.platforms:
                    el.move()
                for el in self.spikes:
                    el.move()
            pg.display.update()    
        
        
            