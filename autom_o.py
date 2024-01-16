class Auto:
    def __init__(self,nev,ev):
        self.nev = nev
        self.ev = int(ev)

    def __str__(self):
        print(f"Az autó neve: {self.nev}, Az autó gyártási éve: {self.ev}")