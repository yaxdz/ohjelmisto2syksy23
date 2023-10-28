import random


class Auto:
    def __init__(self, nimi, nopeus):
        self.nimi = nimi
        self.nopeus = nopeus
        self.matka = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika

    def nopeuden_muutos(self):
        muutos = random.randint(-10, 10)
        self.nopeus = max(0, self.nopeus + muutos)

    def __str__(self):
        return f"{self.nimi} ({int(self.matka)} km)"


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.maaliin_tulleet_autot = []

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.nopeuden_muutos()
            auto.kulje(1)
            if auto.matka >= self.pituus and auto not in self.maaliin_tulleet_autot:
                self.maaliin_tulleet_autot.append(auto)

    def tulosta_tilanne(self):
        print(f"{'Nimi':<15}{'Matka (km)':<15}{'Nopeus (km/h)':<15}")
        for auto in self.autot:
            print(f"{auto.nimi:<15}{int(auto.matka):<15}{int(auto.nopeus):<15}")
        print()

    def kilpailu_ohi(self):
        if self.maaliin_tulleet_autot:
            return True
        else:
            return False



autot = [Auto("Auto1", 100), Auto("Auto2", 110), Auto("Auto3", 120), Auto("Auto4", 130), Auto("Auto5", 140),
         Auto("Auto6", 150), Auto("Auto7", 160), Auto("Auto8", 170), Auto("Auto9", 180), Auto("Auto10", 190)]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

aika = 0
while not kilpailu.kilpailu_ohi():
    if aika % 10 == 0:
        kilpailu.tulosta_tilanne()
    kilpailu.tunti_kuluu()
    aika += 1

kilpailu.tulosta_tilanne()
print("Kilpailu ohi!")