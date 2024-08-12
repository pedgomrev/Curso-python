import math
'''
Para representar valores infinitos en Python, se utilizan las palabras reservadas float('inf') y float('-inf')
para representar infinito positivo e infinito negativo respectivamente.
'''

infinito_positivo = float('inf')
infinito_negativo = float('-inf')

print(f'Infinito positivo: {infinito_positivo}')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito de verdad? : {math.isinf(infinito_positivo)}')
print(f'Es infinito de verdad? : {math.isinf(infinito_negativo)}')

'''
En Python, también se puede representar un valor que no es un número (NaN) con la palabra reservada float('nan').
'''

nan = float('NaN')
print(f'Valor NaN: {nan}')
print(f'Es NaN de verdad? : {math.isnan(nan)}')