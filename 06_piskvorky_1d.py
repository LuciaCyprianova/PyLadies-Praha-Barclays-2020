from random import randrange
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
    print(pole)
    while True:
        pozice = int(input("Na ktorú pozíciu umiestňuješ svoj symbol? "))
        if pozice < 0 or pozice > 19:
            print("Zadaj pozíciu od 0 do 19. Na políčko", pozice, "svoj symbol umiestniť nemôžeš.")
            
        elif pole[pozice] != "-":
            print("Pozícia", pozice, "je už obsadená, musíš zvoliť voľné miesto.")
           
        else:
            pole = tah(pole, pozice, symbol)
            return pole         


def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    print(pole)
    while True:
        pozice = randrange(20)
           
        if pole[pozice] == "-":      
            pole = tah(pole, pozice, symbol)
            return pole  

pole = "---oxxo---xo--------"
symbol = "o"
print("Ťahá počítač: \n", tah_pocitace(pole))