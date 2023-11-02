class Julkaisu:



    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
class lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(self.nimi, self.paatoimittaja)

book = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
book.tulosta_tiedot()
magazine = lehti('Aku Ankka', 'Aki Hyyppä')
magazine.tulosta_tiedot()
