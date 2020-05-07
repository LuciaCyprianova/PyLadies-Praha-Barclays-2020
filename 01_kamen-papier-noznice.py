from random import randrange

print ("Hráme hru: kameň, papier, nožnice")

tah_cloveka = input("Hráš kameň, papier alebo nožnice? (V prípade, že chceš hru ukončiť, napíš 'koniec') ")

while tah_cloveka != "koniec":
    nahoda = randrange(0, 3)
    if nahoda == 0:
        tah_pocitace = "kameň"
    elif nahoda == 1:
        tah_pocitace = "papier"
    else:
        tah_pocitace = "nožnice"

    if (tah_cloveka == "kameň") or (tah_cloveka == "papier") or (tah_cloveka == "nožnice"):

        if (tah_cloveka == "kameň" and tah_pocitace == "nožnice") or (tah_cloveka == "papier" and tah_pocitace == "kameň") or (tah_cloveka == "nožnice" and tah_pocitace == "papier"):
            print ("Počítač dal", tah_pocitace, "Vyhral si! Gratulujem")
            print()
           
        elif (tah_cloveka == tah_pocitace):
            print ("Počítač dal", tah_pocitace, "Remíza!")
            print()

        else:
            print ("Počítač dal", tah_pocitace, "Prehral si :(")
            print()

    else:
        print("Môžeš hrať iba kameň, papier alebo nožnice.")
        print()

    tah_cloveka = input("Hráš kameň, papier alebo nožnice? (V prípade, že chceš hru ukončiť, napíš 'koniec') ")

print("Koniec hry.")