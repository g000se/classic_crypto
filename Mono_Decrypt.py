def monoCipherDecrypt(cipher, key):
    keymap = {}
    plain = []
    
    for i, e in enumerate(key):
        keymap[chr(i + 97)] = e   
        
    keys, values = list(keymap.keys()), list(keymap.values())
     
    for i in cipher:
        if i < 'a' or i > 'z':
            plain.append(i)
            continue
        plain.append(keys[values.index(i)])

    return plain

while 1:
    text = input()
    text = list(text.lower().split())
    cipher = "".join(" " + i for i in text[:-1]).replace(' ', '', 1)
    key = text[-1]
    
    print("".join(monoCipherDecrypt(cipher, key)))
    
#keepgoingnevergiveup qwertyuiopasdfghjklzxcvbnm
#atthugofuftctkuoctxh qwertyuiopasdfghjklzxcvbnm