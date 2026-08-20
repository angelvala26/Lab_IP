numero = 8
if numero == 0:
    print("0")
else:
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        if residuo == 10:
            residuo = "a"
        if residuo == 11:
            residuo = "B"
        if residuo == 12:
            residuo = "C"
        if residuo == 13:
            residuo = "d"
        if residuo == 14:
            residuo = "E"
        if residuo == 15:
            residuo = "f"
        hexadecimal = str(residuo) + hexadecimal
        numero = numero // 16
    print(hexadecimal)