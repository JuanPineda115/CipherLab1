"""
Created on Sat Jul 17 19:49:33 2021

@author: hugo_
"""
#counter para contar las letras del texto plano
from collections import Counter

import matplotlib.pylab as plt

import numpy as np


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


#abecedario 27 letras
abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#Cifrado caesar
def cifrar(cadena, clave):

    texto_cifrado = ''



    for letra in cadena:

        suma = abc.find(letra) + clave

        modulo = int(suma) % len(abc)

        texto_cifrado = texto_cifrado + str(abc[modulo])



    return texto_cifrado

#Decifrado caesar
def decifrar(cadena, clave):



    texto_cifrado = ''



    for letra in cadena:

        suma = abc.find(letra) - clave

        modulo = int(suma) % len(abc)

        texto_cifrado = texto_cifrado + str(abc[modulo])



    return texto_cifrado


#EJEMPLO BASICO
TEXT = "HOLA MUNDO"
clean = cleantext(TEXT)
cif = cifrar(clean,2)
print("Texto cifrado: ",cif)

TextD = "JQNCÑWOFQ"
dec = decifrar(TextD,2)
print("Texto descifrado: " , dec)

#Fuerza BRUTA
cryptic_text = "WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW"
for i in range(0,27):
     plain_text = decifrar(cryptic_text, i)

     print("Para la lleve {}, el texto decifrado: {}".format(i, plain_text))
     
     
    
    
    
# def prob():
#     text2 = "WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW".count("W")
    
#     return text2

# w = prob()
# print("Letra w: ", w)


# def prob(cadena):
#     ocurrencias ={}
    
#     for c in cadena:
#         if c in ocurrencias.keys():
#             ocurrencias[c] +=1
#         else:
#             ocurrencias[c] = 1
            


#Distribucion de probabilidad
a = len(cryptic_text)
# print(a)            
c = Counter(cryptic_text) 
w = c.get("W")
# print(c)
# print(w)

print("***Distribucion probabilidad del texto cifrado***")
# for letra, valor in c.items():
#    prob = valor/a
#    print(letra, ":", prob*100,"%")
   
   
def frecuency(text):
    text = text.upper()
    
    letterF = {}
    
    for letter in abc:
        letterF[letter] = 0
        
    for letter in text:
        if letter in abc:
            letterF[letter] +=1
    return letterF

# def plot(frec):
#     centers = range(len(abc))
#     # plt.bar(centers,frec.values(),align = 'center', tick_label = frec.values())
#     # plt.xlim([0,len(abc) -1])   
#     # plt.show()
#     ypos = range(len(abc))
#     plt.xtics(ypos,abc)
#     plt.bar(ypos,centers)
            
def caesar(Ctext):
    prob = 0
    frec = frecuency(Ctext)
    for letra,valor in frec.items():
        prob = (valor/a)*100
        print(letra, ":", prob,"%")
    
        ypos=range(len(abc))
        plt.xticks(ypos,abc)
        plt.bar(ypos, frec.values())

    # plot(frec)
    
    
caesar(cryptic_text)


#Frecuencias Teoricas

Frec = [13.65,11.79,9.195,7.983,6.696,6.69,6.86,5.27,5.19,4.919,4.802,3.445,3.996,2.925,1.0,0.953,0.693,0.875,1.043,0.585,0.272,0.074,0.022,0.019,0.183,0.523,0.291]
Char = ['E','A','O','S','R','N','I','L','D','C','T','P','U','M','B','F','V','Q','G','H','J','Ñ','K','W','X','Y','Z']  
            
# y= np.arange(len(Frec))
# plt.xticks(y,Frec)
# plt.ylabel("Char")
# plt.title("hhh")
# plt.bar(y,Char)

   
