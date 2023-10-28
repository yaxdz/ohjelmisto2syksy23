class Hissi:
    def __init__(self, numero):
        self.numero = numero
        self.kerros = 1

    def aja(self, kohdekerros):
        if kohdekerros > self.kerros:
            print(f"Hissi {self.numero} nousee kerrokseen {kohdekerros}")
        elif kohdekerros < self.kerros:
            print(f"Hissi {self.numero} laskee kerrokseen {kohdekerros}")
        else:
            print(f"Hissi {self.numero} on jo kerroksessa {kohdekerros}")
        self.kerros = kohdekerros
class Talo:
    def __init__(self, alin_kerroksen_numero, ylimman_kerroksen_numero, hissien_lukumaara):
        self.alin_kerroksen_numero = alin_kerroksen_numero
        self.ylimman_kerroksen_numero = ylimman_kerroksen_numero
        self.hissit = []
        for i in range(hissien_lukumaara):
            hissi = Hissi(i + 1)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.aja(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.aja(1)


talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 9)
talo.aja_hissia(3, 3)

print("Palohälytys!")
talo.palohalytys()
