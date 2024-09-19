#
# print("Je bent in een dungeon! あなたはダンジョンにいます!")
#
#
#
# while True:
#     input_1 = int(input("Welke deur kies je? \n Kies 1 voor de gele deur, 2 voor de rode deur"
#                     " of 3 voor de blauwe deur\n"))
#
#
#         if input_1 == 1:
#             # Ga naar de gele kamer
#             input_2 = int(input("Welke deur kies je nu? Kies 1 voor groen en 2 voor rood."))
#             if input_2 == 1:
#                 groene_kamer = True
#             elif input_2 == 2:
#                 # Ga naar de rode kamer
#             rode_kamer= True
#             else:
#                 print("ongeldige invoer, ga terug naar begin")
#                 #Terugleiden naar het begin
#                 input_1 = int(input("Je bent terug bij het begin! Welke deur kies je?"))
#         elif input_1 == 2:
#             # Ga naar de rode kamer
#             rode_kamer = True
#         elif input_1 == 3:
#             # Ga naar de blauwe kamer
#             input_3 = int(input("Welke deur kies je nu? Kies 1 voor groen en 2 voor rood."))
#             if input_3 == 1:
#                 # Ga naar de groene kamer
#                 groene_kamer = True
#             elif input_3 == 2:
#                 # Ga naar de rode kamer
#                 rode_kamer = True
#             else:
#                 print("ongeldie invoer")
#         else:
#             print("Ongeldige input")
#
#     except (TypeError, ValueError):
#         print("ongeldige invoer, ga terug naar begin")
#
# if(groene_kamer):
#     print("Helaas, je komt een monster tegen en die eet jou op. Je hebt verloren")
#
# if(rode_kamer):
#     print("Je gaat door de groene deur en je komt buiten in de frisse lucht. Gefeliciteerd, je hebt gewonnen")
#
#
# #Zolang er geldige invoer is gaan we door, anders zegt ie "Ongeldige invoer, je blijft in deze kamer!"


print("Het is het jaar 870. Je bent een prinses met een zwaard op een prachtig zwart paard. \n "
      "Je wilt graag leuk leven met vrijheid en blijheid. Je rijdt lekker door het bos en ziet ineens \n "
      "een prins in een toren gevangen zitten met een giga draak eromheen. Wat doe je?")

input_1 = int(input("Kies 1 als je hem gaat redden van de draak, 2 als je hem negeert"
                    " of 3 als je de draak bevriendt\n"))

while input_1 not in [1,2,3]:
    input_1 = int(input("Oeps! Kies opnieuw uit 1 (prins redden), 2 (negeren) of 3 (draak bevrienden: "))

Vrijheid_blijheid = False
Schoonmoeder = False

if input_1 == 1:
    # Je redt de prins
    input_2 = int(input("De prins is zo dankbaar! Hij valt op zijn knieën en biedt je een fortuin en zijn hand aan. Wat doe je nu? \n"
                        "Kies 1 als je het fortuin aanneemt en vrolijk wegloopt. Kies 2 als je het fortuin aanneemt en hem wel wilt trouwen."))
    while input_2 not in [1, 2]:
        input_2 = int(input("Meid, wel kiezen he! Kies 1 (fortuin) of 2 (fortuin en trouwen): "))
    if input_2 == 1:
        # Je neemt het fortuin aan
        Vrijheid_Blijheid = True
    elif input_2 == 2:
        # Je gaat trouwen met de prins
        Schoonmoeder= True
    else:
        print("Meid iets gaat hier maximaal fout, herstart avontuur")
elif input_1 == 2:
    # Je negeert de prins
    Vrijheid_blijheid = True
elif input_1 == 3:
    # Je bevriendt de draak
    input_3 = int(input("Je bevriendt de draak! Ze geeft je de prins daarom als cadeautje, #girlcode. Wat doe je?"
                        "\n Kies 1 als je de prins vrijlaat en 2 als hij best lekker blijkt en je wel wilt trouwen."))
    while input_3 not in [1, 2]:
        input_3 = int(input("Wel kiezen meid! Kies 1 als je de prins vrijlaat en 2 als je hem wilt trouwen: "))
    if input_3 == 1:
        # Ga naar de groene kamer
        Vrijheid_blijheid = True
    elif input_3 == 2:
        # Ga naar de rode kamer
        Schoonmoeder = True
    else:
        print("Meid hier gaat iets fout, herstart je avontuur")
else:
    print("Meid hier gaat iets fout, herstart je avontuur")

if(Vrijheid_blijheid == True):
    print("Eind goed al goed. Heerlijk genieten van je vrijheid.")

if(Schoonmoeder == True):
    print("Oh nee, je schoonmoeder blijkt een enorme tang! Wat een pech, daar gaat je vrijheid EN je blijheid!")


    Hallo dit is extra tekst