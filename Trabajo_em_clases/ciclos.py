#lista
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros: # el número es un nombre temporal para referirse a los elementos de la lista, válido solo dentro de este ciclo
    print(numero)       # los números se imprimirán línea por línea, del 0 al 5

print("_________________________________")
#############################################


numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i = 0
for i in range (i, len(numero), 2):
    #if i%2 == 0:
        print(numero[i])

print("_________________________________")
#############################################

##Diccionarios 
#Clase

persona = {
    'nombre':'Victor',
    'apellido':'Bernal',
    'edad':28,
    'pais':'México',
    'skills':['R', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for llave in persona:
    print(llave)

for llave, valor in persona.items():
    print(llave, valor) # de esta manera obtenemos las claves y los valores impresos