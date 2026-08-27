numero, octal = 8,"" #Se inicializa la variable con un string vacio
if numero == 0: print("0") #Si el numero es 0, imprime directamente 0 
while numero > 0: octal, numero = str( numero % 8)+ octal, numero // 8 # Mientras sea mayor a 0, anade el residuo a OCTAL y divide el numero entre 8 
print(octal) #Imprime la cadena con el resultado final