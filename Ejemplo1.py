for i in range(10):
    numero1 =  int(input("Ingresa un numero no decimal: "))
    numero2 =  int(input("Ingresa un numero no decimal diferente: "))
    numero3 =  int(input("Ingresa un numero no decimal diferente: "))

    if numero1==numero2==numero3:
        print("Los numeros son iguales")

    elif numero1<numero2 and numero1<numero3:
        print(numero1,"es menor") 

    elif numero2<numero1 and numero2<numero3:
        print(numero2,"es menor") 

    elif numero3<numero1 and numero3<numero2:
        print(numero3,"es menor") 

    else:
        print("numeros o valores no válidos")

