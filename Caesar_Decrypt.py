def caesarCipherDecrypt(cipher, key):
    plain = []
    
    for i, e in enumerate(cipher):
        if e < 'a' or e > 'z':
            plain.append(e)
            continue
        
        plain.append(ord(e) - key % 26)
        plain[i] = chr(plain[i] + 26) if plain[i] < 97 else chr(plain[i]) 
        
    return plain

while 1:
    text = input()
    text = list(text.lower().split())
    cipher = "".join(" " + i for i in text[:-1]).replace(' ', '', 1)
    key = text[-1]

    print("".join(caesarCipherDecrypt(cipher, int(key))))

#keepgoingnevergiveup 7
#rllwnvpunulclynpclbw 7