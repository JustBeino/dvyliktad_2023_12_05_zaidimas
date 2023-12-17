#
#
#

m = [[7,8,9],[4,5,6],[1,2,3]]

print(m)
def masyvopic(m):
    for x in m:
        print(x)

m[0][1] = "x"
m[0][2] = "x"
m[0][0] = "x"
print(m[0][1])

for x in m:
    print(x)


def sumuojam(m):
    suma = 0
    for x in m:
        if x == "x":
            suma += 1
    #print(suma)
    return suma

#sumuojam(sumos1eil)


sumos1eil = (m[0][0], m[0][1], m[0][2])     #eilute
sumos2eil = (m[1][0], m[1][1], m[1][2])     #eilute
sumos3eil = (m[2][0], m[2][1], m[2][2])     #eilute
sumos4eil = (m[0][0], m[1][0], m[2][0])     #stulpelis
sumos5eil = (m[0][1], m[1][1], m[2][1])     #stulpelis
sumos6eil = (m[0][2], m[1][2], m[2][2])     #stulpelis
sumos7eil = (m[0][0], m[1][1], m[2][2])     #istrizaine
sumos8eil = (m[2][0], m[1][1], m[0][2])     #istrizaine

#sumuojam(sumos5eil)

sumu_listas = (sumos1eil, sumos2eil, sumos3eil, sumos4eil, sumos5eil, sumos6eil, sumos7eil, sumos8eil)

def arlaimejoX(m):
    for x in sumu_listas:
        n = sumuojam(x)
        if n == 3:
            print("x laimejo")
            return True
        else:
            return False
            print("x dar nelaimejo")
        #return: nugaletojas = 1

def arlygiosios(z):
    lsuma = 0
    for x in z:
        if x == "x" or x == "o":
            lsuma += 1
    if lsuma == 9:
        print("lygiosios")
        return False
    else:
        return True


#m[0][0] = "x"
print(m)

print(arlaimejoX(m))

for x in sumu_listas:
    #sumuojam(x)
    print(x, sumuojam(x))
