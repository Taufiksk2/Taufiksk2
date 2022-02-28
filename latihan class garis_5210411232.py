#5210411232

class Titik:
  def__init__(, x, y):
    self.x = x
    self.y = y

class Garis:
  def__init__(self, titik_pertama, titik_kedua):
    self.titik_pertama = titik_pertama
    self.titik_kedua = titik_kedua

  def panjang(self):
    pjg_x = self.titik_kedua.x - self.titik_pertama.x
    pjg_y = self.titik_kedua.y - self.titik_pertama.y
    pjg = (pjg_x*2 + pjg_y2) * 0.5
    return pjg

titik_a = Titik(0,0)
titik_b = Titik(3,4)
garis_ab = Garis(titik_a,titik_b)
print('pnjang garis ab adalah {}'.format(garis_ab.panjang()))
