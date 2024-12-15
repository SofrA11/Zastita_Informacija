from traceback import print_tb


def binarno(kod):
    """Funkcija koja konvertuje hex u binarni format sa 8 bita."""
    return format(int(kod, 16), '08b')

def obrnuti_endijan(binarno):
    """Funkcija koja obrće bitove za Little Endian format."""
    return binarno[::-1]

def dodaj_nule(binarno, broj_nula):
    """Funkcija koja dodaje nule na kraj binarne vrednosti, prema stepenima polinoma."""
    return binarno + '0' * broj_nula

def XOR(el1,el2):
    if(el1==el2):
        return '0'
    return '1'

def izracunaj_crc(binarno, polinom):
    """Funkcija koja računa CRC vrednost na osnovu polinoma."""
    bin = list(binarno)
    duzina_polinoma = len(polinom)  # Stepen polinoma
    crc = list(polinom)  # Prebacujemo poruku u integer

    # Petlja kroz sve bitove poruke
    for i in range(len(binarno)-duzina_polinoma):
        k = 0
        if bin[i]=='0':
            continue
        print(f'X{i//2} = { ''.join(bin)}')
        tempX = ''.join(bin)
        for j in range(i,i+duzina_polinoma):
            bin[j] = XOR(bin[j],crc[k])
            k+=1

        print(f'CRC = {''.join(crc)}')
        print(f'X{i//2} ⊕ CRC = X{i//2+1}')
        print(f'{tempX} ⊕ {''.join(crc)} = {''.join(bin)}')
        print("------------------------------------------")
    # Vraćamo CRC vrednost u binarnom formatu
    return bin[len(bin)-duzina_polinoma+1:len(bin)]

def podeli_bajtove(unos):
    bajtovi = []
    # Određivanje granice (da li je broj karaktera paran ili ne)
    granica = len(unos) if len(unos) % 2 == 0 else len(unos) - 1

    # Petlja za kreiranje bajtova
    for i in range(0, granica, 2):
        bajtovi.append(unos[i] + unos[i + 1])

    # Ako je unos neparan, dodaj poslednji karakter sa "0" na početku
    if len(unos) % 2 != 0:
        bajtovi.append("0" + unos[-1])

    return bajtovi


def obradi_unos(unos,polinom, significantByte='MSB',endijan='BE'):
    bajtovi = []
    delovi = []
    bajtovi = podeli_bajtove(unos)
    print(bajtovi)
    # Razdvajanje unosa u delove
    if significantByte == 'MSB':
        # MSB: prvo AB, zatim CD, pa 12
        delovi = bajtovi
    elif significantByte=='LSB':
        # LSB: prvo 12, zatim CD, pa AB
        delovi = bajtovi[::-1]  # Kreira kopiju i obrće redosled
    if endijan=='LE':
        print("Unesti format za endian je postavljen na Little Endian")
    elif endijan == 'BE':
        print("Unesti format za endian je postavljen na Big Endian")
    else:
        print("Unesti format za endian nije prepoznat, pa je postavljen Big Endian");
        endijan= 'BE'
    # Procesiranje svakog dela
    rezultati = []
    for deo in delovi:
        if len(deo) == 0:  # Ako je deo prazan, preskoči
            continue
        binarno_deo = binarno(deo)

        # Obrađivanje prema endijanu
        if endijan == 'LE':
            binarno_deo = obrnuti_endijan(binarno_deo)

        # Dodavanje nula prema stepenima polinoma
        binarno_deo = dodaj_nule(binarno_deo, len(polinom) - 1)

        # Računanje CRC
        print(f'Bajt: {deo}')
        print("------------------------------------------")
        crc = izracunaj_crc(binarno_deo, polinom)
        rezultati.append(crc)

    return rezultati

# Testiranje sa unosom 'AB' (MSB i LSB)
#unos = 'AB'
#polinom = '110000111'
# unos = '57'
# polinom = '100000111'
#unos = 'ABCDEF125A' #II Kolokvijum 2023
#polinom = '110000111' #II Kolokvijum 2023
# unos = 'A5F71A2E80' #Januar 2024
# polinom = '1011011' #Januar 2024
unos = 'B3D52D1B80'
polinom = '11000111'
significantByte = 'MSB'
endijan = 'BE'
rezultat = obradi_unos(unos, polinom, significantByte=significantByte, endijan=endijan)
rez = []
for el in rezultat:
    newEl=el
    if(endijan=='LE'):
        newEl = el[::-1]
    bin_string = ''.join(newEl)
    decimal_broj = int(bin_string, 2)
    hex_broj = hex(decimal_broj)
    rez.append(hex_broj)

print(f"CRC za svaki ob bajtova: {rez}")
ZbirniCRC = 0
for hex_value in rez:
    ZbirniCRC ^= int(hex_value, 16)
print(f"Zbirni CRC rezultati u formatu {significantByte} i {endijan} je : {hex(ZbirniCRC)}")
