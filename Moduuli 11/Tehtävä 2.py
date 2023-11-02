
from sahkoauto import Sahkoauto
from polttomoottoriauto import Polttomoottoriauto

sahkokaara = Sahkoauto('ABC-15', 180, 52.5, 20)
icekaara = Polttomoottoriauto('ACD-123', 165, 32.3, 8)

sahkokaara.kiihdyta(50)
sahkokaara.kulje(3)
sahkokaara.testi()
print(sahkokaara.jaljella())

icekaara.kiihdyta(60)
icekaara.kulje(3)
icekaara.testi()
print(icekaara.jaljella())