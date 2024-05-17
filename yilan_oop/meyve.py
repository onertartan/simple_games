import random
import pygame


class Meyve(pygame.Rect):
    def __init__(self,renk, kenar, kenar_sayisi):
        super().__init__( random.randint(0, kenar_sayisi - 1) * kenar,  # x
                          random.randint(0, kenar_sayisi - 1) * kenar,  # y
                          kenar, kenar)     # width, height
        self.renk = renk
        self.kenar = kenar
        self.kenar_sayisi = kenar_sayisi

    def cizdir(self, ekran):
        pygame.draw.rect(ekran, self.renk, self)

    def reset(self):
        self.x = random.randint(0, self.kenar_sayisi-1) * self.kenar
        self.y = random.randint(0, self.kenar_sayisi-1) * self.kenar



