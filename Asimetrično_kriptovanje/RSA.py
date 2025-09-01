from math import gcd

def su_uzajamno_prosti(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1
    
def mod_binary_exponentiation(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent >>= 1
    return result


def rsa(p,q,e,param,crypt):
    
    if(not su_uzajamno_prosti(p,q)):
        return "p i q nisu uzajamno prosti!"
    
    N = p*q
    fi = (p-1)*(q-1)
    
    if(1>e or e>fi):
        return "e mora biti 1<e<fi"
    
    if(not su_uzajamno_prosti(e,fi)):
        return "e i fi moraju da budu uzajamno prosti"
    k=1;
    while((fi*k+1)%e!=0):
        k+=1
    d = (fi*k+1)//e
    
    res=[]
    for el in param:
        if(crypt):
            res.append(mod_binary_exponentiation(el,e,N))
        else:
            res.append(mod_binary_exponentiation(el,d,N))
    return res
#-------#
p = 7
q = 43
e = 5
M = [97,98,99,100]
C = [50]
crypt = True
#-------#

if(crypt):
    print(rsa(p,q,e,M,crypt))
else:
    print(rsa(p,q,e,C,crypt))
