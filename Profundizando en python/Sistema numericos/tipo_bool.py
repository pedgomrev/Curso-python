'''
En Python, el tipo de dato bool se utiliza para representar valores booleanos, es decir, valores de verdad o falsedad.
'''
verdadero = True
falso = False
print(f'Verdadero: {verdadero}')
print(f'Falso: {falso}')
print(type(verdadero))
print(type(falso))

#Trabajando con numeros 0 o 0.0 es falso cualquier otro valor es verdadero
print(f'bool(0): {bool(0)}')
print(f'bool(0.0): {bool(0.0)}')
print(f'bool(1): {bool(1)}')
print(f'bool(10): {bool(10)}')
print(f'bool(-1): {bool(-1)}')

#Trabajando con strings '' es falso cualquier otro valor es verdadero
print(f'bool(""): {bool("")}')
print(f'bool(" "): {bool(" ")}')
print(f'bool("Hola"): {bool("Hola")}')

#Trabajando con listas [] es falso cualquier otro valor es verdadero y con diccionarios {} es falso cualquier otro valor es verdadero
print(f'bool([]): {bool([])}')
print(f'bool([1,2,3]): {bool([1,2,3])}')
print(f"bool({{}}): {bool({})}")
print(f'bool({{1:2,3:4}}): {bool({1:2,3:4})}')
