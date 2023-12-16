#
#
#
import sys

m = [[7,8,9],[4,5,6],[1,2,3]]
zaidejasx = "x"
zaidejaso = "o"

sumos1eil = (m[0][0], m[0][1], m[0][2])     #eilute
sumos2eil = (m[1][0], m[1][1], m[1][2])     #eilute
sumos3eil = (m[2][0], m[2][1], m[2][2])     #eilute
sumos4eil = (m[0][0], m[1][0], m[2][0])     #stulpelis
sumos5eil = (m[0][1], m[1][1], m[2][1])     #stulpelis
sumos6eil = (m[0][2], m[1][2], m[2][2])     #stulpelis
sumos7eil = (m[0][0], m[1][1], m[2][2])     #istrizaine
sumos8eil = (m[2][0], m[1][1], m[0][2])     #istrizaine

sumu_listas = (sumos1eil, sumos2eil, sumos3eil, sumos4eil, sumos5eil, sumos6eil, sumos7eil, sumos8eil)
def masyvopic(m):
    for y in m:
        print(y)

def tikrinam (z, a1, b1, zai):
    if z[a1][b1] != "x" and z[a1][b1] != "o":
        z[a1][b1] = zai
        #masyvopic(z)
        return True
    else:
        print("vieta jau pazymeta")
        #masyvopic(z)
        return False

def tikrinam2 (masel, a, b, zai):
    if tikrinam(masel, a, b) == True:
        masel[a][b] = zai
        masyvopic(masel)
        return (False, masel)
    else:
        return True


def ivedimas(zaid):
    while True:
        match input("Iveskite  1-9\n"):
            case "1":
                print("ivedei 1")
                if tikrinam(m, 2,0, zaid) == True:
                    break
                #masyvopic(m)
            case "2":
                print("ivedei 2")
                if tikrinam(m,2,1, zaid) == True:
                    break
                #masyvopic(m)
            case "3":
                print("ivedei 3")
                if tikrinam(m,2,2, zaid) == True:
                    break
                #masyvopic(m)
            case "4":
                print("ivedei 4")
                m[1][0] = zaid
                #masyvopic(m)
            case "5":
                print("ivedei 5")
                m[1][1] = zaid
                #masyvopic(m)
            case "6":
                print("ivedei 6")
                m[1][2] = zaid
                #masyvopic(m)
            case "7":
                print("ivedei 7")
                m[0][0] = zaid
                #masyvopic(m)
            case "8":
                print("ivedei 8")
                m[0][1] = zaid
                #masyvopic(m)
            case "9":
                print("ivedei 9")
                m[0][2] = zaid
                #masyvopic(m)
            case "\27":
                return exit()
                #sys.exit()
            case _:
                print("ne ta ivedei")
                continue

while True:
    print("zaidejo X ejimas:")
    ivedimas(zaidejasx)
    masyvopic(m)
    print("zaidejo O ejimas:")
    ivedimas(zaidejaso)
    masyvopic(m)





