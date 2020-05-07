def tah(pole, umisteni, symbol):
    '''
    vráti herní pole s daným symbolem umístěným na danou pozici
    vstupem je pole (řetezec), umisteni (integer), symbol (řetezec)
    '''
    pole = pole[:umisteni] + symbol + pole[umisteni + 1:]
    return pole

print(tah("----------", 2, "x"))