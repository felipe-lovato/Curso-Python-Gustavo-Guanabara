#Reproduzir o audio de um arquivo MP3
import pygame

pygame.init()
pygame.mixer.music.load("points.mp3")
pygame.mixer.music.play()
input("Agora você escuta?")
