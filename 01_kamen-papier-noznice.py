print ("Hráme hru: kameň, papier, nožnice")

tah_cloveka = input("Hráš kameň, papier alebo nožnice? ")
tah_pocitace = "kameň"

if (tah_cloveka == "kameň") or (tah_cloveka == "papier") or (tah_cloveka == "nožnice"):

    if (tah_cloveka == "kameň" and tah_pocitace == "nožnice") or (tah_cloveka == "papier" and tah_pocitace == "kameň") or (tah_cloveka == "nožnice" and tah_pocitace == "papier"):
        print ("Počítač dal", tah_pocitace, "Vyhral si! Gratulujem")

    elif (tah_cloveka == tah_pocitace):
        print ("Počítač dal", tah_pocitace, "Remíza!")

    else:
        print ("Počítač dal", tah_pocitace, "Prehral si :(")

else:
    print("Môžeš hrať iba kameň, papier alebo nožnice.")