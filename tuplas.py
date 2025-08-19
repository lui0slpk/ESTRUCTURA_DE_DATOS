# Las tuplas no se pueden modificar después de ser creadas
# Las tuplas son inmutales, no se pueden modificar una vez creadas
# """ las listas se crean con [], las tuplas con ()"""

tupla = (1,2,3,4,5) # Crear una tabla
print("\033[32m Tupla:", tupla, "\033[0m") # Imprimir tupla

# Operaciones de las tuplas
print("\033[33m Logitud de la tupla:", len(tupla), "\033[0m") # Imprimir la longitud de la tupla
print("\033[34m Primer elemento de la tupla:", tupla[0], "\033[0m") # Imprimir el primer elemento de la tupla
print("\033[31m Último elemento de la tupla:", tupla[-1], "\033[0m")
# Buscar un elemento
print("\033[36m Buscar elemento en la tupla:", 3 in tupla, "\033[0m") # Buscar un elemento en la tupla
# Otra forma usando index
print("\033[37m Buscar elemento en la tupla:", tupla.index(3), "\033[0m") # Buscar un elemento en la tupla usando index
# Contar cuantas veces aparece un elemento en la tupla
