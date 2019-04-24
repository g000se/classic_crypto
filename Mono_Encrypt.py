def monoCipherEncrypt(plain, key):
    keymap = {}
    cipher = []
    
    for i, e in enumerate(key):
        keymap[chr(i + 97)] = e   

    for i in plain:
        if i < 'a' or i > 'z':
            cipher.append(i)
            continue
        
        cipher.append(keymap.get(i))
        
    return cipher  

while 1:
    text = input()
    text = list(text.lower().split())
    plain = "".join(" " + i for i in text[:-1]).replace(' ', '', 1)
    key = text[-1]
    
    print("".join(monoCipherEncrypt(plain, key)))
    
#keepgoingnevergiveup qwertyuiopasdfghjklzxcvbnm
#atthugofuftctkuoctxh qwertyuiopasdfghjklzxcvbnm