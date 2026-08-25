numero, binario = 8,"" #Se inicializa la variable con un string vacio
if numero == 0: print("0") #Si el numero es 0, imprime directamente 0
while numero > 0: binario, numero = str( numero % 2)+binario, numero // 2 # Mientras sea mayor a 0, anade el residuo a BINARIO y divide el numero a la mitad
print(binario) # Imprime la cadena con el resultado final