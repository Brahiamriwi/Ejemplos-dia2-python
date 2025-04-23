#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

Invitados = ["Ana","Luis","Sofia"]
nombre = input("Ingrese su nombre: ")

if nombre in Invitados:
    print("Puede entrar")

if nombre not in Invitados:
    print("No puede entrar")    
