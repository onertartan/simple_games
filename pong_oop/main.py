import pygame, sys
from oyuncu import Oyuncu
from top import Top
pygame.init()
saat = pygame.time.Clock()
ekran_gen, ekran_yuk = 640, 480
ekran = pygame.display.set_mode((ekran_gen,ekran_yuk))
pygame.display.set_caption("PONG")
# Oyuncu nesnelerini oluşturma. Yapıcı parametreleri--->    x, y, width, height, renk, hiz, x_yon, y_yon, yukari_tusu, asagi_tusu
oyuncu_gen, oyuncu_yuk = 20, 100
top_gen = top_yuk = 20
oyuncu_1 = Oyuncu(0, (ekran_yuk-oyuncu_yuk)/2, oyuncu_gen, oyuncu_yuk, "red", 5, 0, 0, pygame.K_w, pygame.K_s)
oyuncu_2 = Oyuncu(ekran_gen-oyuncu_gen, (ekran_yuk-oyuncu_yuk)/2, oyuncu_gen, oyuncu_yuk, "red", 5, 0, 0, pygame.K_UP, pygame.K_DOWN)
# top nesnesi oluşturma. Yapıcı parametreleri--->    x, y, width, height, renk, hiz, x_yon, y_yon
top_nesnesi = Top((ekran_gen-top_gen)/2,(ekran_yuk-top_yuk)/2,top_gen,top_yuk,"white",5,1,1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        oyuncu_1.yon_guncelle(event)
        oyuncu_2.yon_guncelle(event)
    oyuncu_1.konum_guncelle(ekran_yuk)
    oyuncu_2.konum_guncelle(ekran_yuk)
    top_nesnesi.konum_guncelle(ekran_yuk)
    top_nesnesi.carpma_kontrol(oyuncu_1, oyuncu_2, ekran_yuk)
    if top_nesnesi.gol_kontrol(ekran_gen):
        oyuncu_1.reset()
        oyuncu_2.reset()
        top_nesnesi.reset()
    # Çizdirme
    ekran.fill("black")
    oyuncu_1.cizdir(ekran)
    oyuncu_2.cizdir(ekran)
    top_nesnesi.cizdir(ekran)
    pygame.display.flip()
    saat.tick(60)

