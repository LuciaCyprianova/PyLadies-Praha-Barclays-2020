def vyhodnotit(pole):
    '''vyhodnotí stav hry piškôrky
    vstupom je reťazec obsahujúci znaky 'x', 'o', '-'
    výstupom je jednoznakový reťazec 'x' (výhra x), 'o' (výhra o), '!'(remíza) alebo '-' (hra pokračuje)
    '''
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

def tah(pole, umisteni, symbol):
    '''
    vráti herní pole s daným symbolem umístěným na danou pozici
    vstupem je pole (řetezec), umisteni (integer), symbol (řetezec)
    '''
    pole = pole[:umisteni] + symbol + pole[umisteni + 1:]
    return pole

def tah_hrace(pole):
    '''
    vstupem je herní pole (řetezec)
    zeptá se hráče, na kterou pozici chce hrát
    ověří proveditelnost operace - daná pozice existuje a ještě není zabraná
    volá funkciu tah
    vrátí herní pole se zaznamenaným tahem hráče
        '''
    while True:        
        try:
            pozice = int(input("Na ktorú pozíciu umiestňuješ svoj symbol? "))      
        except ValueError: 
            print("Musíš zadať číslo!")            
        else:
            if pozice < 0 or pozice > 19:
                print("Zadaj pozíciu od 0 do 19. Na políčko", pozice, "svoj symbol umiestniť nemôžeš.")
                
            elif pole[pozice] != "-":
                print("Pozícia", pozice, "je už obsadená, musíš zvoliť voľné miesto.")
            
            else:
                pole = tah(pole, pozice, 'x')
                return pole 

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    if ("-oo") in pole:
        pole = pole.replace("-oo", "ooo", 1)
        return pole
    elif ("o-o") in pole:
        pole = pole.replace("o-o", "ooo", 1)
        return pole
    elif ("oo-") in pole:
        pole = pole.replace("oo-", "ooo", 1)
        return pole
    elif ("-xx") in pole:
        pole = pole.replace("-xx", "oxx", 1)
        return pole
    elif ("x-x") in pole:
        pole = pole.replace("x-x", "xox", 1)
        return pole
    elif ("xx-") in pole:
        pole = pole.replace("xx-", "xxo", 1)
        return pole
    elif ("o-") in pole:
        pole = pole.replace("o-", "oo", 1)
        return pole
    elif ("-o") in pole:
        pole = pole.replace("-o", "oo", 1) 
        return pole        
    elif ("x-") in pole:
        pole = pole.replace("x-", "xo", 1)
        return pole
    elif ("-x") in pole:
        pole = pole.replace("-x", "ox", 1)
        return pole
    else:
        pozice = pole.index("-")
        pole = tah(pole, pozice, "o")
        return pole

def piskvorky1d():
    '''vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a tah_pocitace, 
    dokud někdo nevyhraje nebo nedojde k remíze
    Kontroluje stav hry po každém tahu
    '''
    pole = "-" * 20
    print(pole)
    while True:
        stav = vyhodnotit(pole)
        if stav != '-':
            break
        else:
            pole = tah_hrace(pole)
            print(pole)
            stav = vyhodnotit(pole)
            if stav != '-':
                break        
            pole = tah_pocitace(pole)
            print("Ťahá počítač:")
            print(pole)    
    return stav       

vysledek = piskvorky1d()
if vysledek == "x":
    print("Gratulujem, vyhral si!")
elif vysledek == "o":
    print("Smola, tentokrát vyhral počítač")
else:
    print("Remíza!")
