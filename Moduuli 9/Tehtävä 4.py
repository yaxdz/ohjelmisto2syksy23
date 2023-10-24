
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        if nopeuden_muutos < 0:
            self.nopeus = max(self.nopeus + nopeuden_muutos, 0)
        else:
            self.nopeus = min(self.nopeus + nopeuden_muutos, self.huippunopeus)

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara

    def __str__(self):
        return f'Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.nopeus} km/h, Matka: {self.matka:.2f} km'

autot = []
for i in range(10):
    rekisteritunnus = f'ABC-{i+1}'
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_jatkuu = True
while kilpailu_jatkuu:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_jatkuu = False
            break

for auto in autot:
        print(auto)