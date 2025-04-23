#definimos la lista

lista = [1,5,6,"hola",10]
valor_abuscar= input("Ingrese el caracter a buscar: ")

if valor_abuscar in lista:
    print(f"El caracter buscado {valor_abuscar},se encuentra en la lista")

else:
    print(f"El caracter buscado {valor_abuscar}, NO se encuentra en la lista")    
