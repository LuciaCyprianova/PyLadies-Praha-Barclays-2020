from random import randrange

hody_max = 0
vitaz = 0

for hrac in range(1, 5):
    
    hod = 0
    pocet_hodov = 0
 
    while hod != 6:
        pocet_hodov = pocet_hodov + 1
        hod = randrange(1, 7)
        print("Hráč", hrac, "hodil číslo", hod)
        
    print()
    print("Hráč", hrac, "hodil", pocet_hodov, "krát")
    print()
   
    if pocet_hodov > hody_max:
        hody_max = pocet_hodov
        vitaz = hrac

print("Vyhral hráč", vitaz)