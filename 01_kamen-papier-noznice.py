print ("Hráme hru: kameň, papier, nožnice")

tah_cloveka = input("kameň, papier alebo nožnice? ")
tah_pocitace = "kameň"

if tah_cloveka == "kameň":
    if tah_pocitace == "kameň":
        print ("Počítač dal", tah_pocitace, "Remíza!")
    elif tah_pocitace == "papier":
        print ("Počítač dal", tah_pocitace, "Prehral si :(")
    else:
        print ("Počítač dal", tah_pocitace, "Vyhral si! Gratulujem")

elif tah_cloveka == "papier":
    if tah_pocitace == "papier":
        print ("Počítač dal", tah_pocitace, "Remíza!")
    elif tah_pocitace == "nožnice":
        print ("Počítač dal", tah_pocitace, "Prehral si :(")
    else:
        print ("Počítač dal", tah_pocitace, "Vyhral si! Gratulujem")   

elif tah_cloveka == "nožnice":
    if tah_pocitace == "nožnice":
        print ("Počítač dal", tah_pocitace, "Remíza!")
    elif tah_pocitace == "kameň":
        print ("Počítač dal", tah_pocitace, "Prehral si :(")
    else:
        print ("Počítač dal", tah_pocitace, "Vyhral si! Gratulujem")

else:
    print("Môžeš hrať iba kameň, papier alebo nožnice.")