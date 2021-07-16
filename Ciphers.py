# Universidad del Valle de Guatemala
# Cifrado de informacion
# Hugo Roman 19199
# Laurelinda Gomez 19501
# Juan Pablo Pineda 19087
# Modulo con los cifrados

#cifrado Caesar
def Caesar(txt):
    print('hola')
    

#cifrado afin
def Afin(txt, ):
    print('hola')

#cifrado Vigenere
def cVigenere(txt, key):
    #calcula la cantidad de caracteres de la llave
    kLength = len(key)
    #convierte la cadena a entero 
    kInt = [ord(i) for i in key]
    #convierte el texto a enteros
    tInt = [ord(i) for i in txt]
    # variable que contendra el texto cifrado
    result = ''

    for i in range(len(txt)):
        v = (tInt[i] + kInt[i % kLength]) % 27
        result += chr(v + 65)
    return result

#descifrado Vigenere
#el texto tiene una clave de 1 a 5 caracteres
def dVigenere(txt, key):
    #calcula la cantidad de caracteres de la llave
    kLength = len(key)
    #convierte la cadena a entero 
    kInt = [ord(i) for i in key]
    #convierte el texto a enteros
    tInt = [ord(i) for i in txt]
    # variable que contendra el texto cifrado
    result = ''

    for i in range(len(txt)):
        v = (tInt[i] - kInt[i % kLength]) % 27
        result += chr(v + 65)
    return result