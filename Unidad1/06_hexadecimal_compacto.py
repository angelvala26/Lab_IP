numero, hexadecimal = 11, "" #Definimos nuestro numero y le damos a hexadecimal una cadena vacia
if numero==0: print("0") #Si el numero es 0, pues imprime 0
while numero > 0: #Inicia un ciclo que se repite mientras el numero sea mayor a 0
    residuo = numero % 16 #Obtiene el residuo al dividir entre el 16
    hexadecimal = "0123456789ABCDEF" [residuo] + hexadecimal #Usa el residuo para buscar el caracter y lo agrega al resultado
    numero = numero // 16 #Se divide el numero entre 16
print(hexadecimal) #Nos muestra el resultadp final de esta conversion
