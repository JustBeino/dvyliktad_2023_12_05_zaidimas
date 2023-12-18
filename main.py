
"""
Užduotis: kryžiukų nuliukų žaidimas (Tic Tac Toe)

daugiau -> info faile
"""
import sys      #gal reiktu jei butu isejimui sys.exit()

m = [[7, 8, 9],[4, 5, 6],[1, 2, 3]]
zaidejasx = "x"
zaidejaso = "o"

def masyvopic(m):
    print(f"  {m[0][0]}  {m[0][1]}  {m[0][2]}")
    print(f"  {m[1][0]}  {m[1][1]}  {m[1][2]}")
    print(f"  {m[2][0]}  {m[2][1]}  {m[2][2]}")

def sumuojam(maseil, zaid):  # cia bus perduota sumos*eil
    suma = 0
    for x in maseil:
        if x == zaid:
            suma += 1
    #print(suma)
    return suma

def arlaimejo(m, zaid):
    sumos1eil = (m[0][0], m[0][1], m[0][2])     #eilute
    sumos2eil = (m[1][0], m[1][1], m[1][2])     #eilute
    sumos3eil = (m[2][0], m[2][1], m[2][2])     #eilute
    sumos4eil = (m[0][0], m[1][0], m[2][0])     #stulpelis
    sumos5eil = (m[0][1], m[1][1], m[2][1])     #stulpelis
    sumos6eil = (m[0][2], m[1][2], m[2][2])     #stulpelis
    sumos7eil = (m[0][0], m[1][1], m[2][2])     #istrizaine
    sumos8eil = (m[2][0], m[1][1], m[0][2])     #istrizaine

    sumu_listas = (sumos1eil, sumos2eil, sumos3eil, sumos4eil, sumos5eil, sumos6eil, sumos7eil, sumos8eil)

    for x in sumu_listas:
        n = sumuojam(x, zaid)
        if n == 3:
            print(f"******************\nZaidejas {zaid} laimejo\n******************")
            return True  # exit()

def tikrinam (z, a1, b1, zai):
    if z[a1][b1] != "x" and z[a1][b1] != "o":
        z[a1][b1] = zai
        return True
    else:
        print("vieta jau pazymeta")
        return False

def ivedimas(zaid):
    while True:
        match input("Iveskite  1-9, 0 lentele, + iseiti\n"):
            case "1":
                print("ivedei 1")
                if tikrinam(m, 2,0, zaid) == True:
                    break
            case "2":
                print("ivedei 2")
                if tikrinam(m,2,1, zaid) == True:
                    break
            case "3":
                print("ivedei 3")
                if tikrinam(m,2,2, zaid) == True:
                    break
            case "4":
                print("ivedei 4")
                if tikrinam(m, 1, 0, zaid) == True:
                    break
            case "5":
                print("ivedei 5")
                if tikrinam(m, 1, 1, zaid) == True:
                    break
            case "6":
                print("ivedei 6")
                if tikrinam(m, 1, 2, zaid) == True:
                    break
            case "7":
                print("ivedei 7")
                if tikrinam(m, 0, 0, zaid) == True:
                    break
            case "8":
                print("ivedei 8")
                if tikrinam(m, 0, 1, zaid) == True:
                    break
            case "9":
                print("ivedei 9")
                if tikrinam(m, 0, 2, zaid) == True:
                    break
            case "+":
                return exit()
                #sys.exit()
            case "0":
                masyvopic(m)
            case _:
                print("ne ta ivedei")
                continue
def arlygiosios(mas):
    lsuma = 0
    for eil in mas:
        for x in eil:
            if x == "x" or x == "o":
                lsuma += 1
    if lsuma == 9:
        print("**********\nlygiosios\n**********")
        return False
    else:
        return True     #kad neiseitu is ciklo while

# --------- programa cia prasideda
print("zaidimas Kryziukai Nuliukai\n-----------------------")
masyvopic(m)
while True:
    print("-----------------------\nDabar zaidejo X ejimas")
    ivedimas(zaidejasx)
    masyvopic(m)
    if arlaimejo(m,zaidejasx) == True:
        break
    if arlygiosios(m) == False:
        break
    print("-----------------------\nDabar zaidejo O ejimas")
    ivedimas(zaidejaso)
    masyvopic(m)
    if arlaimejo(m,zaidejaso) == True:
        break




