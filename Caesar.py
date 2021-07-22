# Universidad del Valle de Guatemala
# Cifrado de informacion
# Hugo Roman 19199
# Laurelinda Gomez 19501
# Juan Pablo Pineda 19087

# counter para contar las letras del texto plano
from collections import Counter
import matplotlib.pylab as plt
import numpy as np

# abecedario 27 letras
abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Cifrado caesar
def cifrar(cadena, clave):
    texto_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[modulo])
    return texto_cifrado

# Descifrado caesar
def decifrar(cadena, clave):
    texto_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) - clave
        modulo = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[modulo])
    return texto_cifrado


def BruteForce():
    cryptic_text = "WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW"
    for i in range(0, 27):
        plain_text = decifrar(cryptic_text, i)
        print("Para la llave {}, el texto decifrado: {}".format(i, plain_text))

    # Distribucion de probabilidad
    a = len(cryptic_text)
    c = Counter(cryptic_text)
    w = c.get("W")

    print("***Distribucion probabilidad del texto cifrado***")

    def frecuency(text):
        text = text.upper()
        letterF = {}
        for letter in abc:
            letterF[letter] = 0
        for letter in text:
            if letter in abc:
                letterF[letter] += 1
        return letterF

    def caesar(Ctext):
        prob = 0
        frec = frecuency(Ctext)
        for letra, valor in frec.items():
            prob = (valor/a)*100
            print(letra, ":", prob, "%")

            ypos = range(len(abc))
            plt.xticks(ypos, abc)
            plt.bar(ypos, frec.values())
    caesar(cryptic_text)

    # Frecuencias Teoricas
    Frec = [13.65, 11.79, 9.195, 7.983, 6.696, 6.69, 6.86, 5.27, 5.19, 4.919, 4.802, 3.445, 3.996,
            2.925, 1.0, 0.953, 0.693, 0.875, 1.043, 0.585, 0.272, 0.074, 0.022, 0.019, 0.183, 0.523, 0.291]
    Char = ['E', 'A', 'O', 'S', 'R', 'N', 'I', 'L', 'D', 'C', 'T', 'P', 'U',
            'M', 'B', 'F', 'V', 'Q', 'G', 'H', 'J', 'Ñ', 'K', 'W', 'X', 'Y', 'Z']