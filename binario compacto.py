numero, binario = 8,""
if numero == 0: print("0")
while numero > 0: binario, numero = str( numero % 2)+binario, numero // 2
print(binario)