numero=int(input("Ingrese un numero: "))
i = 2
primo = 1 
while i < numero:
    if numero % i == 0: 
        primo=0
    i=i+1
if primo==1:
    print("El numero es primo")
if primo==0:
    print("El numero no es primo")
