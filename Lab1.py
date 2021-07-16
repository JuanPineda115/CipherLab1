# Universidad del Valle de Guatemala
# Cifrado de informacion
# Hugo Roman 19199
# Laurelinda Gomez 19501
# Juan Pablo Pineda 19087
# modulo main de pruebas de los cifrados

import Ciphers as enc

def cleantext(txt):
    t = txt.upper()
    t = t.replace("Á", "A")
    t = t.replace("É", "E")
    t = t.replace("Í", "I")
    t = t.replace("Ó", "O")
    t = t.replace("Ú", "U")
    specials = [' ', ',', '.', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for x in specials:
        t = t.replace(x, '')
    return t

prueba = 'hello world'
clean = cleantext(prueba)
print(clean)

cipher = enc.cVigenere(clean, "cinco")
print(cipher)

decipher = enc.dVigenere(clean, "cinco")
print(decipher)
