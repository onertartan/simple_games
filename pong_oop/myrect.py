import pygame
from pygame import Color, draw


class MyRect(pygame.Rect):
    def __init__(self, x, y, width, height, renk, hiz, x_yon, y_yon):
        super().__init__(x, y, width, height)
        self.renk = Color(renk)
        self.hiz = hiz
        self.x_yon = x_yon
        self.y_yon = y_yon
        self.x_baslangic = x
        self.y_baslangic = y

    def cizdir(self, ekran):
        draw.rect(ekran, self.renk, self)

    def reset(self):
        self.x = self.x_baslangic
        self.y = self.y_baslangic

    def konum_guncelle(self, ekran_yuk):
        self.x = self.x + self.x_yon * self.hiz
        self.y = self.y + self.y_yon * self.hiz
        if self.top <= 0:
            self.top = 0
        elif self.bottom >= ekran_yuk:
            self.bottom = ekran_yuk

