from random import randrange

def pohyb(suradnice, strana, ovocie):
    '''dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z")
    přidá k seznamu poslední bod „posunutý“ v daném směru
    v = (1, 0), z = (-1, 0), j = (0, 1), s = (0, -1)
    při pohybu umaže první bod ze seznamu souřadnic. Výsledný seznam tak bude mít stejnou délku,
    jako před voláním
    v případě pohybu ven z mapy nebo pohybu na políčko, které už v seznamu je: 
    výjimka ValueError('Game over')
    přidání 'potravy' Seznam obsahuje na začátku jedno ovoce na políčku, na kterém není had 
    Když had sežere ovoce, vyroste a pokud na mapě zrovna není další ovoce, na náhodném místě (kde není had) vyroste ovoce nové.
    Každých 30 tahů vyroste nové ovoce samo od sebe.
    '''
    
    if suradnice:
        aktualna_suradnica = suradnice[-1]
    else:
        aktualna_suradnica = [0, 0]    
    stlpec = aktualna_suradnica[0]
    riadok = aktualna_suradnica[1]
    if strana == 'v':
        stlpec += 1
    elif strana == 'z':
        stlpec -= 1
    elif strana == 'j':
        riadok += 1
    else:
        riadok -= 1

    if not (0 <= stlpec <= 9 and 0 <= riadok <= 9):
        raise ValueError("Game over!")

    nova_suradnica = (stlpec, riadok)
    if nova_suradnica in suradnice:
        raise ValueError("Game over!")

    suradnice.append(nova_suradnica)
    if nova_suradnica in ovocie:
        poloha_ovocia = ovocie.index(nova_suradnica)
        del ovocie[poloha_ovocia]
        if ovocie == []:
            pridat_ovocie(suradnice, ovocie)                    
    else:         
        del suradnice[0]  
  
def pridat_ovocie(suradnice, ovocie):
    "vegeneruje nové ovocie na mieste, kde nie je had ani iné ovocie"
    while True:
        nove_ovocie = (randrange(10), randrange(10))
        if nove_ovocie not in suradnice and nove_ovocie not in ovocie:
            ovocie.append(nove_ovocie)
            break 

def nakresli_mapu(zoznam_suradnic, ovocie):
    '''dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) 
    vypíše je jako mapu: mřížku 10×10
    na políčka, která jsou v seznamu, napíše X, jinde tečku'''    
    zoznam_zoznamu = []    
    predvoleny_znak = "."
    novy_znak = "X"
    znak_ovocia = "?"
    for podzoznam in range(10):
        podzoznam = []
        for polozka in range(10):
            podzoznam.append(predvoleny_znak)
        zoznam_zoznamu.append(podzoznam)    
    for riadok, stlpec in zoznam_suradnic:
        zoznam_zoznamu[stlpec][riadok] = novy_znak
    for riadok, stlpec in ovocie:
        zoznam_zoznamu[stlpec][riadok] = znak_ovocia
    for radek in zoznam_zoznamu:
        for znak in radek:
            print(znak, end=" ")
        print()

suradnice = [(0, 0), (1, 0), (2, 0)]
ovocie = [(2, 3)]
nakresli_mapu(suradnice, ovocie)
tah = 0
while True:
    strana = input("Zadaj svetovú stranu 's', 'j', 'v' alebo 'z': \nPre ukončenie hry, napíš 'koniec': \n")
    strana = strana.lower().strip()
    if strana in ['s', 'j', 'z', 'v']:
        pohyb(suradnice, strana, ovocie)
        tah = tah + 1
        if tah % 30 == 0:
            pridat_ovocie(suradnice, ovocie)  
        nakresli_mapu(suradnice, ovocie)
    elif strana == 'koniec':
        break
    else:
        print("Takú svetovú stranu nepoznám.")

print('Koniec hry!')