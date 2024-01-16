import random

def lista_letrehoz():
    szamok = []
    for szam in range(1,101,1):
        vSzam = random.randint(1,100)
        szamok.append(vSzam)
    return szamok

def kiir(szamok):
    print(f"A lista elemei: \t{szamok}", end="")


def hettel_oszthato(veletlenSzamok):
    db = 0
    for index in range(1, len(veletlenSzamok), 1):
        if veletlenSzamok % 7 == 1:
            db += 1
            print(f"A listában {veletlenSzamok} darab héttel osztható szám van.")

def masodik():
    veletlenSzamok = lista_letrehoz()
    kiir(veletlenSzamok)
    hettel_oszthato(veletlenSzamok)