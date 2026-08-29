n = int(input("Proporciona un numero: "))
if n <= 1:
    print("No es primo")
i=2
while i <= n: 
    if n % i==0 and i !=2:
      print("No es primo")
      break    
    elif n % i == 0 and i==n:
       print("Es primo")
       break
    elif n%i != 0 and i < n:
       print("Es primo")
       break
    i+= 1
