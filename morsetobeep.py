import pygame
import time

for i in range(100):
    print("\n")


def play_sound(file_path, one_beep_time):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    time.sleep(one_beep_time)
    pygame.quit()


def beeps(file_path, one_beep_time, morse):
    print(morse)
    for string in morse:
        for index in range(len(string)):
            if string[index] == ".":
                play_sound(file_path, one_beep_time * 0.97)
            elif string[index] == "-":
                play_sound(file_path, one_beep_time * 3.0)
            else:
                time.sleep(one_beep_time * 0.41)
        time.sleep(one_beep_time * 6)

