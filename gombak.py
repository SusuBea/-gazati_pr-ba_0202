from Gomba import Gomba
gomba_lista= []

def beolvas():
    fajlom = open("gombak_jav.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    sorok = fajlom.readlines()
    fajlom.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        gomba_lista.append(Gomba(sor))
        i += 1


def gombak_szama():
    print("III/A,B: ")
    print(f"\t A gombak száma: {len(gomba_lista)}")