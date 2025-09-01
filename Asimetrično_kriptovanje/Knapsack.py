def mod_inverz(a, m):
    #x*a = 1 mod m
    # Početne vrednosti za r su m i a
    r_preth = m
    r_tek = a

    # Početne vrednosti za x su 0 i 1
    x_preth = 0
    x_tek = 1

    while r_tek > 0:
        q = r_preth // r_tek

        # Ažuriramo tekuću i prethodnu vrednost niza r
        r_preth, r_tek = r_tek, r_preth - q * r_tek

        # Ažuriramo tekuću i prethodnu vrednost niza x
        x_preth, x_tek = x_tek, x_preth - q * x_tek

    # Proveravamo da li postoji inverz
    if r_preth != 1:
        return None  # Inverz ne postoji

    # Obezbeđujemo da je inverz iz skupa [0, m)
    return (x_preth % m + m) % m

def dekadni_u_binarni_niz(broj):
    # Pretvaranje dekadnog broja u binarni string (bez prefiksa '0b')
    binarni_string = bin(broj)[2:]
    # Konverzija binarnog stringa u listu binarnih cifara (kao int)
    binarni_niz = [int(cifra) for cifra in binarni_string]
    return binarni_niz


def knapsackKriptuj(M,J):
    B = dekadni_u_binarni_niz(M)
    razlika = len(J) - len(B)
    if razlika > 0:
        for i in range(0,razlika):
            B.insert(0,0)
    C = 0
    string_rezultat = ''.join(map(str, B))
    print(f"Poruka M = ({M})10 = ({string_rezultat})2")
    lista = list(zip(J,B))
    result = [x * y for x, y in lista]
    C = sum(result)
    
    expression3 = ' + '.join([f"J[{i}]*B[{i}]" for i in range(len(B))])
    expression = ' + '.join([f"{x}*{y}" for x, y in lista])
    expression2 = ' + '.join([f"{x}" for x in result])
    print(f"C = {expression3}")
    print(f"C = {expression}")
    print(f"C = {expression2}")
    print(f"C = {C}")

    return C
        
def knapsackDekriptuj(C,m_inv, n, P):
    
    # Korak 1: Računamo TC = C * m_inv mod n
    TC = (C * m_inv) % n

    # Korak 2: Predstavljanje TC kao zbira elemenata iz skupa P
    binarni_faktori = []
    for p in reversed(P):
        if TC >= p:
            binarni_faktori.append(1)
            TC -= p
        else:
            binarni_faktori.append(0)
    message=[]
    if TC==0:
        message = ["Mogce je dektiptovati poruku C",True]
    else:
        message = ["Nije moguce dekriptovati poruku C",False]
    # Korak 3: Prevođenje binarnog broja u dekadni sistem
    binarni_faktori.reverse()
    
    expression3 = ' + '.join([f"{P[i]}*{binarni_faktori[i]}" for i in range(len(P))])
    print(f"TC = {expression3}")
    temp = ' + '.join([f"{P[i]*binarni_faktori[i]}" for i in range(len(P)) if P[i] * binarni_faktori[i] != 0])
    
    print(f"TC = {temp} = {(C * m_inv) % n}")
    M = int(''.join(map(str, binarni_faktori)), 2)
    string_rezultat = ''.join(map(str, binarni_faktori))
    print(f"Binarni faktor = ({string_rezultat})2 = ({M})10")

    return M,message
    
    
    
def knapsack(P,m,n,param,kriptuj):
    print(f"P = {P}")
    print(f"m = {m}")
    print(f"n = {n}")
    if(kriptuj):
        print(f"M = {param}")
    else:
        print(f"C = {param}")
    print("----------------------------------------------------------------")
    J = []
    i = 0
    print("Računanje javnog ključa J:")
    for el in P:
        J.append((el*m)%n)
        print(f"J[{i}] = (P[{i}] * m) mod n = ({el}*{m}) mod {n} = {J[i]}")
        i=i+1
    
    print("")
    print(f"J = {J}")
    print("")
    
    print("Računanje multiplikativne inverze im :")
    inverseM = mod_inverz(m,n)
    print(f"im={inverseM}")
    print("")
    C = 0
    M = 0
    if(kriptuj):
        print("Kriptovanje:")
        print("----------------------------------------------------------------")    
        M = param
        C = knapsackKriptuj(M,J)
        print(f"Kriptovana poruka {M} glasi {C}")
    else:
        print("Dekriptovanje:")
        print("----------------------------------------------------------------")   
        C = param
        M,message = knapsackDekriptuj(C,inverseM,n,P)
        if message[1]==True:
            print(message[0])
            print(f"Dekriptovana poruka {C} glasi {M}")
        else:
            print(message[0])
# Glavni program
P = [2,6,9,21,46,99]
m=39
n=194
M = 49
C = 165
knapsack(P,m,n,C,False)
