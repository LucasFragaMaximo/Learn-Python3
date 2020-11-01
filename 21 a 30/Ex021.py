import pygame as pg
pg.init()
pg.mixer_music.load('Olamundo.mp3') #  pg.mixer.music.load('Olamundo.mp3')
pg.mixer.music.play()
pg.event.wait()