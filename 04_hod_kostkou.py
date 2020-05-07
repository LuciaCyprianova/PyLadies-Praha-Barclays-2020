from random import randrange

def hod_kostkou(hrac):
    "vráti počet pokusov, než hráčovi padla 6"
    pocet_hodov = 0
    while True:    
        hod = randrange(1, 7)
        print("Hráč", hrac, "hodil číslo", hod)
        pocet_hodov = pocet_hodov + 1
        if hod == 6:
            print()
            print("Hráč", hrac, "hodil", pocet_hodov, "krát")
            print()
            return pocet_hodov

hody_max = 0
vitaz = 0

for hrac in range(1, 5):        
    pocet_hodov = hod_kostkou(hrac)    
    if pocet_hodov > hody_max:
        hody_max = pocet_hodov
        vitaz = hrac

print("Vyhral hráč číslo", vitaz)