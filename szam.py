import random

def general():
    szam = int(random.random() * 50) + 1
    print("I/A: ")
    print(f"\t A generált szám: {szam}\n")

    print("I/B: ")
    if szam % 5 == 0 and szam % 3 == 0:
        print("\tA szám öttel és hárommal is osztahtó.\n")
    elif szam % 5 ==0:
        print("\tA szám öttel osztahtó.\n")
    elif szam % 3 == 0:
        print("\tA szám hárommal osztahtó.\n")




