import pygame
from myrect import MyRect


class Oyuncu(MyRect):
    def __init__(self, x, y, width, height, renk, hiz, x_yon, y_yon, yukari_tusu, asagi_tusu):
        super().__init__(x, y, width, height, renk, hiz, x_yon, y_yon)
        self.yukari_tusu = yukari_tusu
        self.asagi_tusu = asagi_tusu

    def yon_guncelle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.asagi_tusu:
                self.y_yon = 1
            elif event.key == self.yukari_tusu:
                self.y_yon = -1

        if event.type == pygame.KEYUP:
            if event.key == self.asagi_tusu or event.key == self.yukari_tusu:
                self.y_yon = 0


