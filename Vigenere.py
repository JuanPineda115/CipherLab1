# Universidad del Valle de Guatemala
# Cifrado de informacion
# Hugo Roman 19199
# Laurelinda Gomez 19501
# Juan Pablo Pineda 19087

from numpy.core.fromnumeric import product, repeat
import re


abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar(txt, key):
    result = ""
    kIndex = 0
    for s in txt:
        #desplazamiento
        desp = abc.find(s)
        if desp!=-1:
            desp+=abc.find(key[kIndex])
            desp%=len(abc)
            result += abc[desp].upper()
            kIndex+=1
            if kIndex==len(key):
                kIndex=0
    return result

def decifrar(txt, key):
    result = ""
    kIndex = 0
    for s in txt:
        #desplazamiento
        desp = abc.find(s)
        if desp!=-1:
            desp-=abc.find(key[kIndex])
            desp%=len(abc)
            result += abc[desp].upper()
            kIndex+=1
            if kIndex==len(key):
                kIndex=0
    return result

def frecuency(text):
    text = text.upper()
    letterF = {}
    for letter in abc:
        letterF[letter] = 0
    for letter in text:
        if letter in abc:
            letterF[letter] += 1
    return letterF

def bruteForce(txt):
    keys = []
    possible = []
    for i in range(5):
        prods = list(product(abc, repeat=i))
        for j in prods:
            joins = "".join(i)
            nTry = 'abv'
            try:
                nTry = decifrar(joins, txt)
            except:
                nTry = 'abv'
            probs = frecuency(nTry)