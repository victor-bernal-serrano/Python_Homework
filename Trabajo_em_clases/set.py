#lista = [1, 1, 1]
#tuple = [2, 2, 2]
#sets = {3, 3, 3, 3, 3}
#sets = set (1, 1)

#Frutas = {"platanos", "platanos", "naranja", "mango"}

sets ={1, 1, 2, 1, 1, False, 2}
sets = [2]

print (sets[2])

# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
print("El conjunto st contiene item3? ", 'item3' in st) # El conjunto st contiene item3? True
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
print('mango' in frutas ) # True

#Adición de elementos a un conjunto
#Una vez que se crea un conjunto, no podemos cambiar ningún elemento y también podemos agregar elementos adicionales.

#Agrega un elemento usando add()
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
frutas.add('lime')
#Agregue varios elementos usando update() update() permite agregar varios elementos a un conjunto. El update() toma un argumento de lista.
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
vegetales = ('tomate', 'papa', 'repollo','cebolla', 'zanahoria')
frutas.update(vegetales)
#Eliminación de elementos de un conjunto
#Podemos eliminar un elemento de un conjunto usando el método remove(). Si el elemento no se encuentra, el método remove() generará errores, por lo que es bueno verificar si el elemento existe en el conjunto dado. Sin embargo, el método discard() no genera ningún error.

# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
#el método pop() elimina un elemento aleatorio de una lista y devuelve el elemento eliminado.

#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
frutas.pop()  # elimina un elemento aleatorio del conjunto
#Si estamos interesados ​​en el artículo eliminado

frutas = {'plátano', 'naranja', 'mango', 'limón'}
removed_item = frutas.pop() 
#Borrado de artículos en un conjunto
#Si queremos borrar o vaciar el conjunto, usamos el método clear.

# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
frutas.clear()
print(frutas) # set()
#Borrando un conjunto
#Si queremos eliminar el conjunto en sí, usamos el operador del.

# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
del st
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
del frutas
#Convertir lista en conjunto
#Podemos convertir lista en conjunto y conjunto en lista. La conversión de la lista al conjunto elimina los duplicados y solo se reservarán elementos únicos.

# sintaxis
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - el orden es aleatorio, por que los conjuntos en general estan sin ordenar
#Ejemplo:

frutas = ['plátano', 'naranja', 'mango', 'limón','naranja', 'plátano']
frutas = set(frutas) # {'mango', 'limón', 'plátano', 'naranja'}
##Uniendo conjuntos
#Podemos unir dos conjuntos utilizando los métodos union() o update().

#Union Este método regresa un nuevo conjunto
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
vegetales = {'tomate', 'papa', 'repollo','cebolla', 'zanahoria'}
print(frutas.union(vegetales)) # {'limón', 'zanahoria', 'tomate', 'plátano', 'mango', 'naranja', 'repollo', 'papa', 'cebolla'}
#Update Este método inserta un conjunto en el conjunto dado.
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # se agrega el contenido de st2 a st1
#Ejemplo:

frutas = {'plátano', 'naranja', 'mango', 'limón'}
vegetales = {'tomate', 'papa', 'repollo','cebolla', 'zanahoria'}
frutas.update(vegetales)
print(frutas) # {'limón', 'zanahoria', 'tomate', 'plátano', 'mango', 'naranja', 'repollo', 'papa', 'cebolla'}
#Búsqueda de elementos de intersección
#La intersección devuelve un conjunto de elementos que están en ambos conjuntos. Ve el Ejemplo:

# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
#Ejemplo:

todos_los_numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
todos_los_numeros.intersection(numeros_pares) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
#Comprobación de subconjunto y superconjunto
#Un conjunto puede ser un subconjunto o super conjunto de otro conjunto

Subset: issubset()
#Super set: issuperset
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
#Ejemplo:

todos_los_numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
todos_los_numeros.issubset(numeros_pares) # False, porque es un super conjunto
todos_los_numeros.issuperset(numeros_pares) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
#Comprobando la diferencia entre dos conjuntos
#Regresa la diferencia entre 2 conjuntos

# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
#Ejemplo:

todos_los_numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
todos_los_numeros.difference(numeros_pares) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered el resultado esta sin ordenar (caracteristica de conjuntos)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
#Hallar diferencias simétricas entre dos conjuntos
#Devuelve la diferencia simétrica entre dos conjuntos. Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A)

# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# significa (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
#Ejemplo:

todos_los_numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
algunos_numeros = {1, 2, 3, 4, 5}
todos_los_numeros.symmetric_difference(algunos_numeros) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
#Unión de conjuntos
#Si dos conjuntos no tienen un elemento o elementos comunes, los llamamos conjuntos disjuntos. Podemos verificar si dos conjuntos son conjuntos o disjuntos usando el método isdisjoint().

# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
#Ejemplo:

numeros_pares = {0, 2, 4 ,6, 8}
numeros_pares = {1, 3, 5, 7, 9}
numeros_pares.isdisjoint(odd_numeros) # True, porque no hay elemento común

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, por que hay elementos comunes {'o', 'n'}
