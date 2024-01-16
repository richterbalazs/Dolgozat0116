import autom_o

def beolvas():
    kocsi = []
    beFajl = open("auto.txt", "r", encoding="utf-8")
    beFajl.readline()
    sorok = beFajl.readlines()

    for index in range(0, len(sorok), 1):
        tisztaSorok = sorok[index].strip().split(":")
        peldany = autom_o.Auto(tisztaSorok[0], tisztaSorok[1])
        kocsi.append(peldany)

    beFajl.close()
    return kocsi


def kor(autok):
    print("III/Kor")
    for index in range(1,len(autok),1):
        pass

def flotta(autok):
    print("III/Flotta")
    print(f"\tAutók száma: {len(autok)}")

def ertek(autok):
    print("III/Értékes")
    maximum = 2019
    for index in range(1, len(autok), 1):
        if autok[index].ev > autok[index].ev:
            maximum = index
    print(f"\tA legöregebb autó: {autok}")

def kiiras(autok):
    kiFajl = open("ki.txt", "w", encoding="utf-8")

    kiFajl.close()

def harmadik():
    autok = beolvas()
    kor(autok)
    flotta(autok)
    ertek(autok)