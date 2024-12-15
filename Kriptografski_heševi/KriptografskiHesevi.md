# Funkcija za CRC računanje sa prilagodljivim parametrima

## Funkcija: `obradi_unos`

### Parametri

- **unos**  
  String koji sadrži niz bajtova za koje je potrebno naći CRC. Svaki bajt se sastoji od dve cifre heksadecimalnog brojnog sistema.  
  **Primer:**  
  `unos = 'ABCDEF125A'` se razlaže na bajtove `AB`, `CD`, `EF`, `12`, `5A`.  
  Ukoliko je broj heksadecimalnih cifara neparan, ispred poslednje cifre u nizu dodaje se `0`, kao neutralan element.

- **polinom**  
  String koji predstavlja binarnu vrednost CRC polinoma.  
  **Primer:**  
  Polinom \(X^8 + X^7 + X^2 + X^1 + X^0\) ima binarnu reprezentaciju: `polinom = '110000111'`.

- **significantByte**  
  Određuje da li se radi nad nizom bajtova kod kojih je:  
  - **MSB (Most Significant Byte First)**  
    Bajt najveće težine je prvi u redu.  
    **Primer:**  
    Ako je `unos = 'ABCDEF125A'`, CRC će se računati za bajtove redom:  
    1. `AB = 0000000001101010 = 0x6a`  
    2. `CD = 0000000110110110 = 0xb6`  
    3. `EF = 0000000100000010 = 0x2`  
    4. `12 = 0000000001010100 = 0x54`  
    5. `5A = 0000000100000100 = 0x4`  

  - **LSB (Least Significant Byte First)**  
    Bajt najmanje težine je prvi u redu.  
    **Primer:**  
    Ako je `unos = 'ABCDEF125A'`, CRC će se računati za bajtove redom:  
    1. `5A = 0000000100000100 = 0x4`  
    2. `12 = 0000000001010100 = 0x54`  
    3. `EF = 0000000100000010 = 0x2`  
    4. `CD = 0000000110110110 = 0xb6`  
    5. `AB = 0000000001101010 = 0x6a`  

- **endijan**  
  Određuje kako su raspoređeni bitovi unutar svakog bajta.  
  - **Big Endian**  
    Bit najveće težine je levo.  
    **Primer:**  
    Za heksadecimalni broj `AB`: `10101011`.  

  - **Little Endian**  
    Bit najveće težine je desno.  
    **Primer:**  
    Za heksadecimalni broj `AB`: `11010101`.  

### Objašnjenje Big Endian i Little Endian formata
- **Big Endian:**  
  `AB → 10101011`  
- **Little Endian:**  
  `AB → 11010101`  

Za detaljnije objašnjenje pogledajte video: [Endianness Explained](https://youtu.be/WBA6svOyWb8?si=VXCbw-e9bcdQS4wZ)
