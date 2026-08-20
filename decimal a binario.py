numero = 8
if numero == 0:
    print("0")
else:
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    print(binario)