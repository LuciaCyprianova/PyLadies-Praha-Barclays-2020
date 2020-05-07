from turtle import forward, left, exitonclick, penup, pendown

def nakresli_n_uholnik(pocet_stran):
    uhel = 180 * (1 - 2 / pocet_stran)
    delka_strany = 200 / pocet_stran
    for n_uholnik in range(pocet_stran):
        forward(delka_strany)
        left(180 - uhel)
    
for n in range(5, 9):
    nakresli_n_uholnik(n)
    penup()
    forward(80)
    pendown()

exitonclick()