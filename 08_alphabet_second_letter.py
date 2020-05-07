def abecedne_bez_prveho_pismena(zoznam):
    'seřadí podle abecedy, ale bude ignorovat první písmeno'
    rozsireny_zoznam = []
    for zviera in zvierata:
        kluc_zviera = zviera[1:]
        dvojice = (kluc_zviera, zviera)
        rozsireny_zoznam.append(dvojice)

    zoradeny_zoznam = sorted(rozsireny_zoznam)

    novy_zoznam = []
    for zviera in zoradeny_zoznam:
        novy_zoznam.append(zviera[1])
    return novy_zoznam

zvierata = ['had', 'pes', 'andulka', 'mačka', 'králik']
print('pôvodný zoznam:\n{}'.format(", ".join(zvierata)))

zvierata2 = abecedne_bez_prveho_pismena(zvierata)
print('zoznam zoradený abecedne podľa druhého písmena slova:\n{}'.format(", ".join(zvierata2))