# Universidad del Valle de Guatemala
# Cifrado de informacion
# Hugo Roman 19199
# Laurelinda Gomez 19501
# Juan Pablo Pineda 19087
# para el inverso si utilizó esta página https://www.geeksforgeeks.org/implementation-affine-cipher/

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


def inverso(l, s):
    z,y, u,v = 0,1, 1,0
    while l != 0:
        q, t = s//l, s%l
        m, n = z-u*q, y-v*q
        s,l, z,y, u,v = l,t, u,v, m,n 
    resp1 = s
    return resp1, z, y
 
def modulo(l, m):
    resp1, z, y = inverso(l, m)
    if resp1 != 1:
        return None 
    else:
        return z % m
 
#  cipher text
def encrypt(text, key):

    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# original text
def decrypt(cipher, key):
   
    return ''.join([ chr((( modulo(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])


def main():
    #  text and key
    text = 'HELLO WORLD'
    key = [17, 20]

    #  encryption 
    encrypted = encrypt(text, key)
    print('Encrypted: {}'.format( encrypted ))

    #  decryption 
    print('Decrypted: {}'.format
    ( decrypt(encrypted, key) ))

 
if __name__ == '__main__':
    main()


# Fuerza Bruta

