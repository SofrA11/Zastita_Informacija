from email import message_from_string
from operator import concat


def hmac(key, message, opad, ipad):
    # Koristi opad i ipad prema specifikaciji
    blocksize = len(key)
    opad = bytes([opad] * blocksize)
    ipad = bytes([ipad] * blocksize)

    # Skrati ključ ako je duži od blocksize
    if len(key) > blocksize:
        key = hash(key)  # Očekuje se da funkciju hash korisnik definiše

    # Dopuni ključ nulama ako je kraći od blocksize
    if len(key) < blocksize:
        key = key + bytes([0x00] * (blocksize - len(key)))

    # Primeni XOR operacije
    res1 = bytes([b ^ k for b, k in zip(ipad, key)]) #ipad XOR K
    res1 = res1 + message
    res1Hout = hash(res1)
    print(res1Hout.hex())

    res2 = bytes([b ^ k for b, k in zip(opad, key)])
    res2 = res2 + res1Hout

    res2Hout = hash(res2)
    # Kombinuje vrednosti prema HMAC algoritmu
    return res2Hout

def hash(input_bytes):#Januar2024

    hash_value = input_bytes[0] | 0xE7
    pom = 0
    for i in range(1, len(input_bytes)):
        hash_value = hash_value ^ ((i % 0xA) ^ input_bytes[i - 1])
        pom=i
    return bytes([hash_value])

def hash2(input_bytes):#April 2023
    hash_value = input_bytes[0] | 0xCC
    for i in range(1, len(input_bytes)):
        hash_value = hash_value ^ ((i % 0xC) ^ input_bytes[i - 1])

    return bytes([hash_value])
key = bytes.fromhex("29AA")
message = bytes.fromhex("AA678823AABF12")
res = hmac(key,message , 0xA6,0x6A)
print(res.hex())