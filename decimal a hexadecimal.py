numero, hexadecimal = 10, ""
if numero==0: print("0")
while numero>0:
    residuo=numero%16
    if residuo==10:
        hexadecimal=str("A")+ hexadecimal
    elif residuo==11:
        hexadecimal=str("B")+ hexadecimal
    elif residuo==12:
        hexadecimal=str("C")+ hexadecimal
    elif residuo==13:
        hexadecimal=str("D")+ hexadecimal
    elif residuo==14:
        hexadecimal=str("E")+ hexadecimal
    elif residuo==15:
        hexadecimal=str("F")+ hexadecimal
    elif residuo < 10:
        hexadecimal = str(residuo)+ hexadecimal 
    numero = numero // 16
print(hexadecimal)