import pygame, sys
from yilan import Yilan
from meyve import Meyve

pygame.init()
saat = pygame.time.Clock()
ekran_gen, ekran_yuk = 400, 400
ekran = pygame.display.set_mode((ekran_gen, ekran_yuk))
pygame.display.set_caption("YILAN")

kenar = kenar_sayisi = 20  # ekran_gen = ekran_yuk = kenar*kenar_sayisi
yilan = Yilan("red","white", kenar, kenar_sayisi)
meyve = Meyve("green",kenar, kenar_sayisi)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        yilan.yon_guncelle(event)
    yilan.konum_guncelle()

    ekran.fill("black")
    meyve.cizdir(ekran)
    yilan.cizdir(ekran)
    if yilan.carpma_kontrol():
        yilan.reset()
        meyve.reset()
    if yilan.meyve_yeme_kontrol(meyve):
        meyve.reset()

    pygame.display.flip()
    saat.tick(3)

