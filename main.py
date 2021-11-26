import pygame
import numpy as np
from pygame.constants import *
import threading

from sorting import sorting

(w, h) = (512, 512)
bg_color = (0, 0, 0)
obj_color = {0:(255, 255, 255), 1:(0, 255, 0), 2:(255, 0, 0), 3:(0, 0, 255)}

size = 64
data = sorting(size, write_delay=0.005)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Test')
pygame.key.set_repeat(1000, 50)

running = True

while running:
    screen.fill(bg_color)

    # rendering
    for i in range(0, size):
        pygame.draw.rect(screen, obj_color[data.anno[i]], pygame.Rect(i * w / data.size, h - (data.array[i] * h / data.size), w / size, data.array[i] * h / data.size))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_s:
                print('Shuffle')
                thread = threading.Thread(target=getattr(data, 'shuffle'))
                thread.start()

            if event.key == K_d:
                print('Shuffle slightly')
                thread = threading.Thread(target=getattr(data, 'shuffle'), args=(0.1,))
                thread.start()

            if event.key == K_f:
                print('Reverse')
                thread = threading.Thread(target=getattr(data, 'reverse'))
                thread.start()
            
            if event.key == K_a:
                print('Check sorted')
                thread = threading.Thread(target=getattr(data, 'check_sorted'))
                thread.start()
                
            if event.key == K_q:
                print('Stop')
                data.clear_anno()

            if event.key == K_z:
                data.is_sorting = True
                print('Bubble sort')
                thread = threading.Thread(target=getattr(data, 'bubble_sort'))
                thread.start()

            if event.key == K_x:
                data.is_sorting = True
                print('Insertion sort')
                thread = threading.Thread(target=getattr(data, 'insertion_sort'))
                thread.start()

            if event.key == K_c:
                data.is_sorting = True
                print('Shaker sort')
                thread = threading.Thread(target=getattr(data, 'shaker_sort'))
                thread.start()

            if event.key == K_v:
                data.is_sorting = True
                print('Selection sort')
                thread = threading.Thread(target=getattr(data, 'selection_sort'))
                thread.start()
            if event.key == K_b:
                data.is_sorting = True
                print('Shell sort')
                thread = threading.Thread(target=getattr(data, 'shell_sort'))
                thread.start()

            if event.key == K_n:
                data.is_sorting = True
                print('Sandwich sort')
                thread = threading.Thread(target=getattr(data, 'sandwich_sort'))
                thread.start()

data.is_sorting = False