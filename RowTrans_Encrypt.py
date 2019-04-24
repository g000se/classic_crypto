def rowTransEncrypt(plain, key):
    ciphermap = [[int(i)] for i in key]
    cipher = []

    for i, e in enumerate(plain):
        ciphermap[i % len(key)].append(e)
        
    ciphermap = sorted(ciphermap)
    
    for i in ciphermap:
        cipher.extend(i[1:])
        
    return cipher
    
while 1:
    text = input()
    text = text.lower()
    for i in text:
        if i >= '0' and i <='9':
            plain = text[:text.index(i) - 1]
            key = text[text.index(i):]
            break    
    key = list(key.split())
    
    print("".join(rowTransEncrypt(plain, key)))
    
#keepgoingnevergiveup 3 1 5 6 2 4 8 7
#enegekgvoreeupvpniig 3 1 5 6 2 4 8 7