def vernamAutokeyEncrypt(plain, key):
    cipher = []
    plainbin = []
    keybin = []
  
    for i in key:
        keybin.append(ord(i) - 97)
    
    for i in plain:
        plainbin.append(ord(i) - 97)
    
    keybin += plainbin[:len(plainbin) - len(keybin)]

    for i, j in zip(plainbin, keybin):
        cipher.append(chr((i ^ j) + 97))
    return cipher

while 1:
    text = input()
    text = list(text.lower().split())
    plain = "".join(i for i in text[:-1])
    key = text[-1]
    
    print("".join(vernamAutokeyEncrypt(plain, key)))
    
#keepgoingnevergiveup con
#ikjfckhlifjtjvtmecca con