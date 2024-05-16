from myrect import MyRect


class Top(MyRect):
    def __init__(self, x, y, width, height, renk, hiz, x_yon, y_yon):
        super().__init__(x, y, width, height, renk, hiz, x_yon, y_yon)

    def carpma_kontrol(self, oyuncu1, oyuncu2, ekran_yuk):
        if self.colliderect(oyuncu1) or self.colliderect(oyuncu2):
            self.x_yon = -self.x_yon
        if self.top <= 0 or self.bottom >= ekran_yuk:
            self.y_yon = -self.y_yon

    def gol_kontrol(self,ekran_gen):
        if self.left <= 0 or self.right >= ekran_gen:
            return True
        else:
            return False
