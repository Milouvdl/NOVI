# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.

small = 15
medium = 20
large = 25

bestelling = ""
bestelling = str.lower(bestelling)

tot_prijs = 0
formaat = input("Hoe groot wil je je pizza? \n Typ s voor small, m voor medium of l voor large: ")
formaat = str.lower(formaat)
if formaat == "s":
    tot_prijs += 15
    bestelling += "kleine pizza "
elif formaat == "m":
    tot_prijs += 20
    bestelling += "medium pizza "
elif formaat == "l":
    tot_prijs += 25
    bestelling += "grote pizza "
else:
    print("Verkeerd getypt")
print(f"Je hebt een {bestelling} gekozen. \n Dit is de prijs van je pizza nu: {tot_prijs}")
pepperoni = input("Wil je pepperoni op je pizza? Typ 1 voor ja, typ 2 voor nee: ")
pepperoni = int(pepperoni)
if pepperoni == 1:
    bestelling += "met pepperoni "
    if formaat == "s":
        tot_prijs += 2
    if formaat == "m" or formaat == "l":
        tot_prijs += 3
elif pepperoni == 2:
    bestelling += "zonder pepperoni "
    tot_prijs += 0

print(f"Je hebt een {bestelling} gekozen. \n Dit is de prijs van je pizza nu: {tot_prijs}")
kaas = input("Wil je er kaas op? Kies 1 voor ja, kies 2 voor nee: ")
kaas = int(kaas)
if kaas == 1:
    bestelling += "met kaas"
    tot_prijs += 1
elif kaas == 2:
    bestelling += "zonder kaas"
    tot_prijs += 0

print(f"Je hebt {bestelling} gekozen. Goede keus! \n Dit is je totaalprijs: {tot_prijs}. Geniet van je pizza!")
