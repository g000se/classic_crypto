import string

def playfairCipherEncrypt(plain, key):
    keymap = []
    plainmap = []
    cipher = []
    
    for i in key.replace('j', 'i'):   #key -> keymap, 'j' -> 'i'
        if i not in keymap: keymap.append(i)
    
    for i in list(string.ascii_lowercase):  #keymap append except 'j'
        if i not in key and i != 'j': keymap.append(i)
    
    for i in range(0, len(plain), 2):
        if plain[i] == plain[-1]:
            plain.append('x') if len(plain) % 2 else plain
        elif plain[i] == plain[i + 1]:
            plain.insert(i + 1, 'x')
            i = 0
                
    plainmap = plain
    
    for i in range(0, len(plainmap), 2):  #mapping
        first_w, second_w = keymap.index(plainmap[i]), keymap.index(plainmap[i + 1])
        
        if first_w // 5 == second_w // 5: #same row
            first_w = first_w + 1 if first_w % 5 != 4 else first_w - 4
            second_w = second_w + 1 if second_w % 5 != 4 else second_w - 4
        elif first_w % 5 == second_w % 5:    #same column
            first_w = first_w + 5 if first_w < 20 else first_w - 20
            second_w = second_w + 5 if second_w < 20 else second_w - 20
        else:   #diagonal
            diagonal = first_w + second_w
            first_w = (first_w // 5) * 5 + second_w % 5
            second_w = diagonal - first_w
        
        cipher.extend([keymap[first_w], keymap[second_w]])
        
    return cipher

while 1:
    text = input()
    text = list(text.lower().split())
    plain = "".join(i for i in text[:-1])
    key = text[-1]
    
    print("".join(playfairCipherEncrypt(list(plain), key)))
    
#keepgoingnevergiveup hit
#mccroualfocxmxdbxcpq hit
#h, i, t, a, b
#c, d, e, f, g
#k, l, m, n, o
#p, q, r, s, u
#v, w, x, y, z