def caesarCipherEncrypt(plain, key):
    cipher = []
    
    for i, e in enumerate(plain):
        if e < 'a' or e > 'z':
            cipher.append(e)
            continue 
        
        cipher.append(ord(e) + (key % 26))
        cipher[i] = chr(cipher[i] - 26) if cipher[i] > 122 else chr(cipher[i])
        
    return cipher

while 1:
    text = input()
    text = list(text.lower().split())
    plain = "".join(" " + i for i in text[:-1]).replace(' ', '', 1)
    key = text[-1]
    
    print("".join(caesarCipherEncrypt(plain, int(key))))
    
#keepgoingnevergiveup 7
#rllwnvpunulclynpclbw 7