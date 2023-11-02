from auto import Auto


class Sahkoauto(Auto):
    def __init__(self, rekkari ,huiput, kapasiteetti, kulutus):
        super().__init__(rekkari, huiput, kulutus)
        self.kapasiteetti = kapasiteetti
        self.kulutus = kulutus

    def jaljella(self):
        return (self.kapasiteetti - super().kulutettu())

    def testi(self):
        print(f'''Rekkari: {self.rekkari}, Huippunopeus : {self.huippunopeus}),
        kuljettu matka : {self.matka}, tämän matkan nopeus: {self.nopeus}, kulutus:{self.kulutettu()}''')