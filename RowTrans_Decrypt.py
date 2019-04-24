def rowTransDecrypt(cipher, key):
    plainmap = [[int(i)] for i in sorted(key)]
    plain = []
    m = divmod(len(cipher), len(key))
    count = 0
    
    for i, e in enumerate(sorted(key)):
        mod = m[0] + 1  if key.index(e) < m[1] else m[0]
        plainmap[i].extend(cipher[count:count + mod])
        count += mod
        
    for i in range(len(cipher)):
       plain.append("")
       plain[i] = plainmap[sorted(key).index(key[i % len(key)])].pop(1)
    
    return plain
   
while 1:
    text = input()
    text = text.lower()
    for i in text:
        if i >= '0' and i <='9':
            key = text[text.index(i):]
            cipher = text[:text.index(i) - 1]
            break
    key = list(key.split())
    key = [int(i) for i in key]
    
    print("".join(rowTransDecrypt(cipher, key)))
    
#keepgoingnevergiveup 3 1 5 6 2 4 8 7
#enegekgvoreeupvpniig 3 1 5 6 2 4 8 7