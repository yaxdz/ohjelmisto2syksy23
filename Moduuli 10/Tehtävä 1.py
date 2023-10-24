class Auto:
    def __init__(self, input_rekkari, input_huiput):
        self.rekisteritunnus = input_rekkari
        self.huippunopeus = input_huiput
        self.nopeus = 0
        self.matka = 0


from auto import Auto
import random

kaara = Auto('ABC-123', 142)


class Auto:
    def __init__(self, rekkari, huiput):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


autot = []
for i in range(10):
    rekisteritunnus = f'ABC-{i + 1}'
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))


def kulje(self, tunnit):
    self.matka = self.nopeus * tunnit
    self.matka += self.nopeus * tunnit


kilpailu_jatkuu = True
while kilpailu_jatkuu:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_jatkuu = False
            break
for auto in autot:
    print(auto)