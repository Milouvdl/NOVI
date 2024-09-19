g# # ==========================================
# # Voorbeeld Opdracht
# # Gebruik de not operator om het tegenovergestelde van de boolean waarde True te printen.
# # ==========================================
#
# print(not True)     # Het resultaat is: False
#
#
# # ==========================================
# # Opgave 1.
# # Gebruik logische operatoren om te controleren of het getal 5 zowel groter is dan 3 als kleiner dan 10.
# # Print het resultaat.
# # Controleer daarna of 5 groter is dan 10 of gelijk is aan 5.
# #
# # Verwachte uitkomst is de boolean waarde: True
# # ==========================================
#
# x = 5
# print(x>3 and x<10)
# print(x>10 or x==5)
#
#
#
# # ==========================================
# # Opgave 2.
# # Evalueer of het getal 7 zowel groter is dan 5 als kleiner dan 12, en tegelijkertijd niet gelijk is aan 10.
# # Print het resultaat.
# #
# # Verwachte uitkomst: True
# # ==========================================
#
# x=7
# print(x>5 and x<12 and x!=10)
#
# # ==========================================
# # Opgave 3
# # Gegeven is x = 5 en y = -5
# # Gebruik logische operatoren om te controleren of de variabelen positief zijn en kleiner dan 10. Print het resultaat als boolean waarde.
# #
# # Verwachte uitkomst voor x is: True
# # Verwachte uitkomst voor y is: False
# # ==========================================
#
# x = 5
# y = -4
# print(x >= 0 and x < 10)
# print(y >= 0 and y < 10)
# print(" ")
#
#
# # ==========================================
# # Opgave 5.
# # Geef aan wat het resultaat zou zijn van de volgende code:
#
# # A. print(True or 1 / 0)
# # B. print(True or False)
# # C. print(False and True and True)
# # D. print(True or False or False)
# # E. print(not True or False or not True)
# # ==========================================
#
# print(True or 1 / 0)
# print(True or False)
# print(False and True and True)
# print(True or False or False)
# print(not True or False or not True)


# ==========================================
# Opgave 6:
# Evalueer of een nummer even of oneven is.
# Maak een variabele 'nummer' aan met de waarde 42,
# Schrijf de evaluatie die bepaalt of het nummer even of oneven is. Print de string 'Even' als het nummer even is, anders print 'Oneven'.
# Tip: Als het nummer gedeeld door 2 geen restwaarde heeft, dan is het even. Anders is het oneven.
# ==========================================

x = 46
if (x %2) == 0:
    print("Even")
else:
    print("Odd")

# ==========================================
# Opgave 7:
# Begroeting op Basis van het Uur van de Dag
#
# Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9).
# Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond".
# Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, zeg "Goedemorgen"; als het minder dan 18 is, zeg "Goedemiddag"; en anders, zeg "Goedenavond".
# Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn. Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.
#
# Check het resultaat met de print() methode. Veranderde de waarde van 'uur' om te zien of de begroeting verandert.
# ==========================================

# import datetime as dt
# dt = dt.datetime.now()
# print(dt)

uur = 9

if (uur < 12):
    print("Goedemorgen!")
elif (uur >= 12 and uur < 18):
    print("Goedemiddag!")
else:
    print("Goedenavond!")

# =========================================
# Opgave 8:
# Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren. Print daarna de som en het product van de getallen.
# De input functie moet vragen 'Voer eerste getal in :' en 'Voer tweede getal in :'
# Zorg ervoor dat de input ook kommagetallen accepteert.
#
# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================
#
# Getal_1 = input("Zeg eens een getal")
# Getal_2 = input("Zeg nog eens een getal")
# Getal_1 = float(Getal_1)
# Getal_2 = float(Getal_2)
# print(Getal_1+Getal_2)
#
# a=45
# a+=5
# print(a)
#
# a = 5
# print(type(a), a)
# a = float(a)
# print(type(a), a)
# a=int(5.0)
# print(type(a), a)
# a=int(6.7)
# print(type(a), a)
# voorbeeld_een = int("8")
# print(type(voorbeeld_een), voorbeeld_een)
# a = str(6.7)
# print(type(a), a)
#
# naam = "Milou"
# leeftijd = 30
# print(f"Mijn naam is {naam} en ik ben {30} jaar oud!")
# a=5
# b=10
# print(f"Vijf plus tien is {a+b}")

# ==========================================
# Voorbeeld Opdracht
# Gegeven is een variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn leeftijd is 25'
# ==========================================
#
# leeftijd = 25
# print('Mijn leeftijd is', leeftijd)  # Het resultaat is: Mijn leeftijd is 25
#
# # ==========================================
# # Opgave 1.
# # Gegeven is een variabele 'naam' met de waarde 'Jan' en de variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn naam is Jan en ik ben 25 jaar oud'. Verander daarna de leeftijd naar 30 en print de zin opnieuw.
# #
# # Verwachte uitkomst is: 'Mijn naam is Jan en ik ben 25 jaar oud' en 'Mijn naam is Jan en ik ben 30 jaar oud'
# # ==========================================
#
# naam = 'Jan'
# leeftijd = 25
# print(f"Mijn naam is {naam} en ik ben {leeftijd} jaar oud!")
#


# ==========================================
# Opgave 2.
# Gegeven zijn een aantal variabelen. Wat zijn de datatypes van de variabelen als je ze print met de type() method? Bedenk vooraf wat het datatype is en controleer daarna met de print functie of je het goed hebt.
# ==========================================

# a = 5 / 5
# print(type(a), a)
# b = '12'
# print(type(b), b)
# c = 5 * 5
# print(type(c), c)
# d = 'Python' * 4
# print(type(d), d)

# ==========================================
# Opgave 3.
# Variabele namen mag je zelf verzinnen, maar niet alle namen zijn toegestaan omdat ze al gebruikt worden door Python (keywords). Welke van de volgende variabele namen zijn toegestaan en welke niet?
# ==========================================
#
#
# and = 'something'
# while = 'something'
# break = 'something'
# awaiting = 'something'
#


# ==========================================
# Opgave 4.
# Schrijf een goede variabele naam voor onderstaande onderdelen. Denk aan de conventies voor Python variabelen.
#
# a.     Het totale aantal van het product bananen in een winkelmand
#
# b.     De minimale toegestane lengte voor een attractie in een pretpark
#
# c.     Het grootste getal in een rij met getallen
# ==========================================

totaal_bananen_mand = 10
minimun_lengte_achtbaangast = 1.35
hoogste_getal = 8

# ==========================================
# Opgave 5.
# Gegeven is de variabele 'teller' met de waarde 10. Verhoog de waarde van de teller met 1. Gebruik de samengevoegde toekenning operator. Print de waarde van de teller. Herhaal dit proces maar verlaag de teller met 2. Print opnieuw de waarde van de teller.
#
# Verwachte uitkomst is: 11 en 9
# ==========================================

teller = 10
teller -= 1
print(teller)
teller = 10
teller += 1
print(teller)


# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’)
# Foutmelding want haakjes om een integer maakt het een string
# b. print(float(12))
# Prima, dan krijg je 12.0
# c. print(int('1plus1'))
# Foutmelding want hier staat tekst in, kan ie geen integer van maken
# d. print(str(25E10))
# Dit doet ie wel, je krijgt hier gewoon de tekst '25E10' denk ik --> Oh nee, hij maakt er een uitgetypt getal van
# ==========================================

print(int(1409.99))
print(float(12))
print(int(1+1))
print(str(25E10))


# ==========================================
# Opgave 7.
# Gegeven is de variabele getal_1 met waarde 3 en getal_2 met waarde 5. Schrijf de zin 'Het product van 3 en 5 is 15' door de variabelen te gebruiken in de zin. Pas een f-string toe.
# ==========================================

getal_1 = 3
getal_2 = 5
print(f"Het product van {getal_1} en {getal_2} is {getal_1*getal_2}")