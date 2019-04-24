def productCipherDecrypt(cipher, transport):
    transport = [int(i) - 1 for i in transport]
    k = len(transport)
    plain = [''] * len(cipher)
    
    for i in range(len(plain)):
        plain[transport[i % k] + k * (i // k)] = cipher[i]
    
    return ("".join(plain))

while 1:
    text = input()
    text = text.lower()
    for i in text:
        if i >= '0' and i <='9':
            cipher = text[:text.index(i) - 1]
            transport = text[text.index(i):]            
            break
    transport = list(transport.split())
    
    print(productCipherDecrypt(cipher, transport))
#keepgoingnevergiveup 15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08
#geueieireppvgokgvenn 15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08