class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
            if self.nopeus < 0:
                self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.nopeus * tunnit
        self.matka += self.nopeus * tunnit



    def testi(self):
        print(f'''Rekkari: {self.rekkari}, Huippunopeus : {self.huippunopeus}),
        kuljettu matka : {self.matka}, tämän matkan nopeus: {self.nopeus}''')


    def __str__(self):
        return f'Rekisteritunnus: {self.rekkari}, Huippunopeus: {self.huippunopeus} km/h, Nopeus: {self.nopeus} km/h, Matka: {self.matka:.2f} km'