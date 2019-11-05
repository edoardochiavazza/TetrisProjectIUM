#Python games for IUMProject
import configparser

import pygame

RGB_COLORS = [
    [0, 0, 0],  # NERO
    [0, 204, 255],  # AZZURRINO
    [102, 255, 51], # VERDE
    [255, 51, 0], # ROSSO
    [204, 153, 255], # VIOLA
    [255, 255, 0],  # GIALLO
    [255, 153, 0],  #arancio
    [0, 102, 255]  # blu
]

PIECES_TETRIS = [
    [[1, 1, 1]],

    [[2, 0, 0],
     [2, 2, 2]],

    [[0, 0, 3],
     [3, 3, 3]],

    [[4, 4],
     [4, 4]],

    [[0, 5, 5],
     [5, 5, 0]],

    [[6, 6, 0],
     [0, 6, 6]],

    [[0, 7, 0],
     [7, 7, 7]]
]

class Tetris:
    def read_config(section, field):
        if not hasattr(read_config, "config"):
            read_config.config = configparser.ConfigParser()
            read_config.config.read("config.ini")
        return read_config.config.get(section, field)


def main():
    pygame.init()
    pygame.key.set_repeat(250, 25)
    cell_size = int(read_config('playground', 'cell_size'))
    width = int(read_config('playground', 'cols')) * cell_size
    height = int(read_config('playground', 'rows')) * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.event.set_blocked(pygame.MOUSEMOTION)


if __name__ == '__main__':
    main()
