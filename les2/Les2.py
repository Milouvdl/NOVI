# leeftijd = (int(input("Hoe oud ben je")))
# print(f"Jouw leeftijd is {leeftijd}")
#
# getal = int(input("Noem eens een getal: "))
# print(f"Jouw getal maal 5 is dit: {getal*5}")

# ==========================================
# # Voorbeeld Opdracht
# # Gebruik de not operator om het tegenovergestelde van de boolean waarde True te printen.
# # ==========================================
#
# print(not True)     # Het resultaat is: False
#

# ==========================================
# Opgave 1.
# Gebruik logische operatoren om te controleren of het getal 5 zowel groter is dan 3 als kleiner dan 10.
# Print het resultaat.
# Controleer daarna of 5 groter is dan 10 of gelijk is aan 5.
#
# Verwachte uitkomst is de boolean waarde: True
# ==========================================
#
# x = 5
# print(x>3 and x<10)
#
# # ==========================================
# # Opgave 2.
# # Evalueer of het getal 7 zowel groter is dan 5 als kleiner dan 12, en tegelijkertijd niet gelijk is aan 10.
# # Print het resultaat.
# #
# # Verwachte uitkomst: True
# # ==========================================
#
# # x = 7
# # (x>5 and x!=10)
#
# # ==========================================
# # Opgave 3
# # Gegeven is x = 5 en y = -5
# # Gebruik logische operatoren om te controleren of de variabelen positief zijn en kleiner dan 10. Print het resultaat als boolean waarde.
# #
# # Verwachte uitkomst voor x is: True
# # Verwachte uitkomst voor y is: False
# # ==========================================
# #
# # x = 5
# # y = -4
# #
# # print(x >=0 and x<10)
# # print(y >=0 and y<10)
#
#
# # ==========================================
# # Opgave 5.
# # Geef aan wat het resultaat zou zijn van de volgende code:
# #
# # print("Hieronder opgave 5")
# # print(True or 1 / 0)
# # print(True or False)
# # print(False and True and True)
# # print(True or False or False)
# # print(not True or False or not True)
# # # ==========================================
# #
# # True
# # True
# # False
# # True
# # False
# # #BOOM goed!!
#
# # ==========================================
# # Opgave 6:
# # Evalueer of een nummer even of oneven is.
# # Maak een variabele 'nummer' aan met de waarde 42,
# # Schrijf de evaluatie die bepaalt of het nummer even of oneven is. Print de string 'Even' als het nummer even is, anders print 'Oneven'.
# # Tip: Als het nummer gedeeld door 2 geen restwaarde heeft, dan is het even. Anders is het oneven.
# # ==========================================
#
# nummer = 57
# nummer %2
# if nummer % 2 == 0:
#     print("Even!")
# else:
#     print("Oneven!")
#
# # ==========================================
# # Opgave 7:
# # Begroeting op Basis van het Uur van de Dag
# #
# # Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9).
# # Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond".
# # Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, zeg "Goedemorgen"; als het minder dan 18 is, zeg "Goedemiddag"; en anders, zeg "Goedenavond".
# # Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn. Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.
# #
# # Check het resultaat met de print() methode. Veranderde de waarde van 'uur' om te zien of de begroeting verandert.
# # ==========================================
#
# uur = 18.5
#
# if uur <=12:
#     print("Goedemorgöhn")
# elif uur >12 and uur <=18:
#     print("Goedemiddâhg")
# elif uur >18 and uur <=24:
#     print("Goedenahffônd")
#
#
# # =========================================
# # Opgave 8:
# # Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren. Print daarna de som en het product van de getallen.
# # De input functie moet vragen 'Voer eerste getal in :' en 'Voer tweede getal in :'
# # Zorg ervoor dat de input ook kommagetallen accepteert.
# #
# # Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# # ==========================================
#
# Getal1 = float(input("Noem eens een lekker getalletje: "))
# Getal2 = float(input("Noem nog eens een lekker getalletje: "))
# print(f"Als je die bij elkaar doet krijg je {Getal1 + Getal2}, leuk hè?")
#
# # ==========================================
# # Voorbeeld Opdracht
# # Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# # ==========================================
#
# a = 3
# b = 10
#
# if a > b:
#     print(a)
# else:
#     print(b)

# ==========================================
# Opgave 1:
# Gegeven is een int input getal_1 en getal_2 en drie print methodes. Schrijf een if statement dat controleert of getal1 een veelvoud
# is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================
#
#
# getal_1 = int(input("voer een getal in: "))
# getal_2 = int(input("voer een getal in: "))
#
# if getal_1 % getal_2 == 0 and getal_1 != getal_2:
#     print("Getal 1 is een veelvoud van getal 2!")
# elif getal_2 % getal_1 == 0 and getal_2 != getal_1:
#     print("Getal 2 is een veelvoud van getal 1!")
# elif getal_2 % getal_1 != 0 and getal_2 != getal_1 and getal_1 % getal_2 != 0:
#     print("Getal 1 en getal 2 zijn geen veelvoud van elkaar.")
# else:
#     print("Oeps, er is wat fout gegaan")
#

# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================
#
# prijs = 12
# leeftijd = int(input("voer je leeftijd in: "))
# if leeftijd <5:
#     print(f"Als je jonger dan 5 bent kom je gratiesj, betaal maar {prijs-prijs}")
# elif leeftijd >=5 and leeftijd <=12:
#     print(f"Als je tussen 5 en 12 bent betaal je de helft, betaal dan {prijs / 2}")
# elif leeftijd >12 and leeftijd <55:
#     print(f"Grote mensen betalen volle prijs, pannekoek, betaal maar {prijs}")
# elif leeftijd >=55:
#     print(f"Oude mensen zijn weer gratiesj ouwe, betaal maar {prijs-prijs}")
#

# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de
# variabelen num1, num2 en num3 (maak deze variabelen met inputs zelf aan).
# Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================
#
# getal_1 = int(input("Noem eens een getal: "))
# getal_2 = int(input("Noem nog eens een getal: "))
# getal_3 = int(input("Noem NOG eens een getal: "))
#
# # print(getal_1, getal_2, getal_3)
# # if getal_1 < getal_2 and getal_1 < getal_3:
#     getal_1 = str("laagste")
#     if getal_2 < getal_1 and getal_2 < getal_3:
#         getal_2 = str("laagste")
#         if getal_3 < getal_1 and getal_3 < getal_2:
#             getal_3 = str("laagste")
# if getal_1 < getal_2 or getal_3 and getal_1 > getal_2 or getal_3:
#     middelste = getal_1
#     if getal_2 < getal_1 or getal_3 and getal_2 > getal_1 or getal_3:
#         middelste = getal_2
#         if getal_3 < getal_1 or getal_2 and getal_3 > getal_2 or getal_2:
#             middelste = getal_3
# if getal_1 > getal_2 and getal_1 > getal_3:
#     hoogste = getal_1
#     if getal_2 > getal_1 and getal_2 > getal_3:
#         hoogste = getal_2
#         if getal_3 > getal_1 and getal_3 > getal_2:
# #             hoogste = getal_3
# #
# # print(laagste, middelste, hoogste)
#
# print(getal_1, getal_2, getal_3)
# if (getal_1 < getal_2 < getal_3):
#     print(getal_1, getal_2, getal_3)
# elif (getal_1 < getal_3 < getal_2):
#     print(getal_1, getal_3, getal_2)
# elif(getal_2 < getal_1 < getal_3):
#     print(getal_2, getal_1, getal_3)
# elif(getal_2 < getal_3 < getal_1):
#     print(getal_2, getal_3, getal_1)
# elif(getal_3 < getal_2 < getal_1):
#     print(getal_3, getal_2, getal_1)
# elif(getal_3 < getal_1 < getal_2):
#     print(getal_3, getal_1, getal_2)
# else:
#     print("HELP DIT GAAT FOUT")
#
#
#
#


# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0.
# Schrijf een programma dat herhaaldelijk een getal als input vraagt.
# Elk getal dat je invoert moet moet worden opgeteld bij het totaal.
# Als je 0 invoert moet het programma stoppen en met een print statement het totaal
# en het gemiddelde van de getallen afdrukken (dus totaal / aantal inputs).
# Als er geen getallen zijn ingevoerd moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================
# #
#
# totaal = 0
# aantal_inputs = 0
# a = int(input("Noem eens een cijfer (als je wil stoppen zeg je 0):"))
#
# while a > 0 :
#     totaal += a
#     aantal_inputs += 1
#     print("bij elkaar is dat", totaal)
#     a = int(input("Noem eens een cijfer:"))
#
# print("Bij elkaar is dat",totaal,", je hebt", aantal_inputs, "cijfers ingevoerd en het gemiddelde is", (totaal/aantal_inputs),".")
#



# totaal = 0
# getal1 = int(input("Noem eens een getal: "))
# while getal1 != 0 :
#     totaal += 1
#     print(totaal + getal1)
#     getal = int(input("Noem eens een getal: "))
#     if getal1 == 0:
#         break
#         print(totaal)





# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt, Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15    # enz. tot en met 10
# ==========================================
#
# factor = int(input("Noem eens een heel getal onder de 10: "))
# y = 1
# while y<=10:
#     print(f"{(y)} x {factor} = {(y)*factor}")
#     y += 1

#BOEM HET IS GELUKT!!