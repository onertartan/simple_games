import pygame
from pygame import Color, Rect, draw


class Yilan:
    def __init__(self, bas_renk, govde_renk, kenar, kenar_sayisi):
        self.bas_renk = Color(bas_renk)
        self.govde_renk = Color(govde_renk)
        self.kenar = kenar # hız: her güncellemede bir kenar uzunluğu kadar yer değiştirecek
        self.kenar_sayisi = kenar_sayisi
        self.x_yon = 1
        self.y_yon = 0
        self.hucreler = [ Rect(self.kenar * self.kenar_sayisi / 2, self.kenar * self.kenar_sayisi / 2, self.kenar, self.kenar)]

    def cizdir(self, ekran):
        draw.rect(ekran, self.bas_renk, self.hucreler[0])
        for i in range(1, len(self.hucreler)):
            draw.rect(ekran, self.govde_renk, self.hucreler[i])

    def basa_yeni_hucre_ekle(self):
        eski_bas = self.hucreler[0]
        yeni_bas = pygame.Rect(eski_bas.x + self.x_yon * self.kenar, eski_bas.y + self.y_yon * self.kenar,self.kenar, self.kenar)
        self.hucreler.insert(0, yeni_bas)

    def konum_guncelle(self):
        self.basa_yeni_hucre_ekle()  # baş hücrenin önüne yeni hücre ekle
        self.hucreler.pop()  # listenin sonundaki hücreyi listeden çıkar

    def yon_guncelle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.x_yon, self.y_yon = 0, -1
            elif event.key == pygame.K_DOWN:
                self.x_yon, self.y_yon = 0, 1
            elif event.key == pygame.K_RIGHT:
                self.x_yon, self.y_yon = 1, 0
            elif event.key == pygame.K_LEFT:
                self.x_yon, self.y_yon = -1, 0

    def carpma_kontrol(self):
        bas = self.hucreler[0]
        # Eğer bas hücresi gövde hücrelerinden birine çarparsa True döndürür.
        for hucre in self.hucreler[1:]:
            if bas.colliderect(hucre):
                return True
        # Eğer ekranın sol, sağ, üst veya alt çizgiyi geçiyorsa True döndürür.
        if bas.left < 0 or bas.right > self.kenar*self.kenar_sayisi or bas.top < 0 or bas.bottom > self.kenar*self.kenar_sayisi:
            return True
        # Eğer üstteki if'lere girilmediyse çarpma olmamış demektir. False döndürüyoruz.
        return False

    def reset(self):
        self.hucreler = [Rect(self.kenar * self.kenar_sayisi / 2, self.kenar * self.kenar_sayisi / 2, self.kenar, self.kenar)]

    def meyve_yeme_kontrol(self, meyve):
        # hucreler listesinin (self.hucreler) ilk  elemanı, meyve ile çarpışıyorsa
        # listenin başına yeni hücre eklesin ve True döndürsün, aksi takdirde False döndürsün
        meyve_yedi_mi = self.hucreler[0].colliderect(meyve)
        if meyve_yedi_mi:
            self.basa_yeni_hucre_ekle()
        return meyve_yedi_mi