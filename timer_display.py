#!/usr/bin/env python
import pygame
import os
from termcolor import colored

def seconds(time):
    duration = time.split(':')

    if len(duration) != 3:
        print "INVALID INPUT! QUITTING......"
        quit()
    else:
        for i in [0,1,2]:
            duration[i] = int(duration[i])

    total_seconds = ((duration[0]*3600) + (duration[1] * 60) + duration[2])
    return total_seconds


def display_box(time,title):
    pygame.init()
    width = 240
    height = 100
    displayer = pygame.display.set_mode((width,height))
    pygame.display.set_caption("***POMODORO TIMER ***" + "***TASK: " + title + "***")
    font = pygame.font.SysFont('cooperblack', 35)

    total_seconds = seconds(time)

    def countdown(time):
        seconds = time%60
        minutes = ((time/60)%60)
        hours = (time/3600)

        return "%i : %i : %i "%(hours,minutes,seconds)

    
    while total_seconds > 0:
        if total_seconds <= 30:
            displayer.fill((255,255,255))

        else:
            displayer.fill((255,255,255))

        string = countdown(total_seconds)

        font_position = ((0.5*width) - (0.5 * font.size(string)[0]),
                         (0.5*height) - (0.5 * font.size(string)[1]))

        rendered_font = font.render(string, 1,(0,0,0))
        displayer.blit(rendered_font,font_position)
        pygame.display.flip()
        pygame.time.wait(1000)
        total_seconds -=1
    pygame.quit()



display_box('00:00:15','EAT')
    