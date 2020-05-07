def faktorial(n):
    "vráti hodnotu n! zo zadaného čísla"
    sucin = n
    for i in range(1, n):
        sucin = sucin * (n - i)        
    return sucin
    

def prvocislo(n):
    "určí, či sa jedná o prvočíslo, vráti True alebo False"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    "vypíše prvých n-členov postupnosti"
    cislo1 = 0
    cislo2 = 1
    print("Prvých {} členov Fibonacciho postupnosti je: ".format(n))
    print(cislo2, end=" ")
    for i in range(n - 1):
        cislo3 = cislo1 + cislo2
        print(cislo3, end=" ")
        cislo1 = cislo2
        cislo2 = cislo3
    print()   

while True:
    n = int(input("Zadaj hodnotu čísla n: "))
    print()
    if n > 0:    
        break
    else:
        print("Zadaj prosím kladné číslo.")

n_faktorial = faktorial(n)
prvocislo = prvocislo(n)

print("{}! = {}".format(n, n_faktorial))
if prvocislo:
    print("Číslo {} je prvočíslo".format(n))
else:
    print("Číslo {} nie je prvočíslo".format(n))
fibonacci(n)