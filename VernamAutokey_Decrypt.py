def vernamAutokeyDecrypt(cipher, key):
    plain = []
    cipherbin = []
    keybin = []
    
    for i in key:
        keybin.append(ord(i) - 97)
    
    for i in cipher:
        cipherbin.append(ord(i) - 97)
        
    for i, j in zip(cipherbin, keybin):
        plain.append(chr(((i ^ j)) + 97))
        keybin.append((i ^ j) % 26)
        
    return plain

while 1:
    text = input()
    text = list(text.lower().split())
    cipher = "".join(i for i in text[:-1])
    key = text[-1]
    
    print("".join(vernamAutokeyDecrypt(cipher, key)))
    
#keepgoingnevergiveup con
#ikjfckhlifjtjvtmecca con