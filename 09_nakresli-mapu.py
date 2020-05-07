def nakresli_mapu(zoznam_suradnic):
    '''dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) 
    vypíše je jako mapu: mřížku 10×10
    na políčka, která jsou v seznamu, napíše X, jinde tečku'''    
    zoznam_zoznamu = []    
    predvoleny_znak = "."
    novy_znak = "X"
    for podzoznam in range(10):
        podzoznam = []
        for polozka in range(10):
            podzoznam.append(predvoleny_znak)
        zoznam_zoznamu.append(podzoznam)    
    for riadok, stlpec in zoznam_suradnic:
        zoznam_zoznamu[stlpec][riadok] = novy_znak
    for radek in zoznam_zoznamu:
        for znak in radek:
            print(znak, end=" ")
        print()

def pohyb(suradnice, strana):
    '''dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z")
    přidá k seznamu poslední bod „posunutý“ v daném směru
    v = (1, 0), z = (-1, 0), j = (0, 1), s = (0, -1)'''
    if suradnice:
        aktualna_suradnica = suradnice[-1]
    else:
        aktualna_suradnica = [0, 0]
    
    stlpec, riadok = aktualna_suradnica
    
    if strana == 'v':
        stlpec += 1
    if strana == 'z':
        stlpec -= 1
    if strana == 'j':
        riadok += 1
    if strana == 's':
        riadok -= 1  
    suradnice.append((stlpec, riadok))

suradnice = [(0, 0)]
nakresli_mapu(suradnice)
while True:
    strana = input("Zadaj svetovú stranu 's', 'j', 'v' alebo 'z': \nKeď bude mapa hotová, napíš 'hotovo': \n")
    strana = strana.lower()
    strana = strana.strip()
    if strana == 's' or strana == 'j' or strana == 'v' or strana == 'z':
        tah = pohyb(suradnice, strana)
        if tah == False:
            print("Súradnica mimo rozsah, zadaj prosím inú stranu.")            
        else:
            nakresli_mapu(suradnice)
    elif strana == 'hotovo':
        break
    else:
        print("Takú svetovú stranu nepoznám.")

print('Koniec hry, pekná mapa!')