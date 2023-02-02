korok = []

def beker():
    i = 0
    szoveg = ""
    while i < 5:
        kor = int(input("Add meg a korod: "))
        korok.append(kor)
        if i == 4:
            szoveg += str(kor)
        else:
            szoveg += str(kor) + " : "
        i += 1
    print("II/A, B, C:")
    print(f"\t{szoveg}")
    elso_idos(korok)

def elso_idos(korok):
    i = 0
    index = -1
    while i < len(korok):
        if korok[i] > 70:
            index = i
        i += 1
    return index

def konzolra_kiir():
    print("II/D,E: ")
    print(f"Az első idős ember korának a helye a listában: {elso_idos(korok)}")


def fajlba_ir():
    fajlom = open("oreg.txt", "w", encoding="utf-8")
    fajlom.write(f"kimutatas.txt tartalma:\n II/F:\n\t Az első idős ember korának a helye a listában: {elso_idos(korok)}")
    fajlom.close()


