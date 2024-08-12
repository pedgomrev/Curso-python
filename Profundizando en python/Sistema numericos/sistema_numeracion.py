#Profundizando en los sistemas de numeración
# En este script se muestra cómo convertir un número de un sistema de numeración a otro.

#Binario
binario = 0b1010
print(f'binario 1010 : {binario}') # 10

#Octal
octal = 0o12
print(f'Octal 12 : {octal}') # 10

#Hexadecimal
hexadecimal = 0xA
print(f'Hexadecimal A : {hexadecimal}') # 10

#Otra manera de convertir un número a otra base
numero = 10
numero5 = int('10',5)
print(f'Numero 10 en base 5: {numero5}') # 5
#funcion para convertir un numero a otras bases binario,octal y hexaxecimal

def convertir_a_base(numero,base):
    if base == 2:
        return bin(numero)
    elif base == 8:
        return oct(numero)
    elif base == 16:
        return hex(numero)
    else:
        return 'Base no soportada'
    
print(convertir_a_base(10,2)) # 0b1010
print(convertir_a_base(10,8)) # 0o12
print(convertir_a_base(10,16)) # 0xa