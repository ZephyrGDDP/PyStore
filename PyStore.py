import pygame
import pgzero
import pgzrun
import webbrowser
from pygame.locals import *
from pygame import mixer

WIDTH = 800
HEIGHT = 800
btn = Rect(75, 100, 100, 50)
btn2 = Rect(185, 100, 100, 50)
btn99 = Rect(10, 680, 100, 50)
str1 = ("1")

pygame.display.set_caption("PyStore - The Open-Source Python Store")

def on_key_down(key):
    if key == keys.W:
                file1 = open("storesave.txt","w+")
                file1.write(str1)
                if FileNotFoundError:
                    file1 = open("storesave.txt","a")

mixer.init()
mixer.music.load(filename='Kevin MacLeod - BossaBossa.mp3')
mixer.music.play(loops=-1)
pycoins  = open("storesave.txt","r")
print(pycoins)

def draw():
    screen.fill('black') 
    screen.draw.rect(btn, 'red') 
    screen.draw.text("Download", (85, 115), color = 'red') 
    screen.draw.rect(btn2, 'red') 
    screen.draw.text("Download", (195, 115), color = 'red')
    screen.draw.text("Classic Arcade Collection - Pong", (70, 100))
    screen.draw.rect(btn99, 'red')

def on_mouse_down(pos, button):
    if btn.collidepoint(pos):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=CllgCJvnJjjGfrmDRjlrvvbdKnFLZQwqspGCmzHbsDSqpkFfpbcHzCcGDwnCDgLBfFbbjnhqbzL")
    
    if btn2.collidepoint(pos):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=CllgCJqXPXTKqBqgbbTzzcLGxLcCccsVwJgqxDCTfgVTpTgNXwflSbwlzlVKsfcbNFCkqlchkDV")


pgzrun.go()    
