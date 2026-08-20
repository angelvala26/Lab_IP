numero = 8
if numero == 0:
    print("0")
else:
    octal = ""
    while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero = numero // 8
    print(octal)