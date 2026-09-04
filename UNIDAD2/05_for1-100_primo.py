for numero in range(1,101):
    if numero%numero==0 and numero%1==0 and (numero%2!=0 and numero%3!=0 and numero%5!=0 and numero%7!=0) and numero!=1 or numero==2 or numero==3 or numero==5 or numero==7:
        print(numero)