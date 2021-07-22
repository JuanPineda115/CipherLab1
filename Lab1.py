# Universidad del Valle de Guatemala
# Cifrado de informacion
# Hugo Roman 19199
# Laurelinda Gomez 19501
# Juan Pablo Pineda 19087
# modulo main de pruebas de los cifrados

import Caesar as cs
import Afin as af
import Vigenere as vg

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

# EJEMPLO BASICO CAESAR
print("\nEjemplos basicos de cifrado y descifrado")
print("\nMetodo: Caesar\nTexto: Hola Mundo\nClave: 2")
TEXT = "HOLA MUNDO"
clean = cleantext(TEXT)
cif = cs.cifrar(clean, 2)
print("Texto cifrado: ", cif)
dec = cs.decifrar(cif, 2)
print("Texto descifrado: ", dec, "\n")

# EJEMPLO BASICO VIGENERE
print("\nMetodo: Vigenere\nTexto: Hola Mundo\nClave: nueva")
TEXT = "Hola Mundo"
clean = cleantext(TEXT)
cif = vg.cifrar(clean, "nueva")
print("Texto cifrado: ", cif)
dec = vg.decifrar(cif, "nueva")
print("Texto descifrado: ", dec, "\n")

# EJEMPLO BASICO Afin
print("\nMetodo: Afin\nTexto: Hola Mundo\nClave: nueva")
TEXT = "Hola Mundo"
clean = cleantext(TEXT)
cif = vg.cifrar(clean, "nueva")
print("Texto cifrado: ", cif)
dec = vg.decifrar(cif, "nueva")
print("Texto descifrado: ", dec, "\n")

print("Descifrando los textos proveidos con fuerza bruta:")
print("\nCaesar")
cs.BruteForce()
print("Vigenere")
vg.BruteForce()