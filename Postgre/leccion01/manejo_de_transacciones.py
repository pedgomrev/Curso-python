import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(
                            user = 'postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'Test_db'
                        )

try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sql = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            # Valores a insertar
            nombre = input("Proporciona el nombre: ")
            apellido = input("Proporciona el apellido: ")
            email = input("Proporciona el email: ")
            valores = (nombre, apellido, email)
            cursor.execute(sql, valores)

            sql2 = 'UPDATE persona SET nombre = %s WHERE id_persona = %s'
            valores2 =  input("Proporciona el nuevo nombre: "),input("Proporciona el id de la persona: ")
            cursor.execute(sql2, valores2)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    print("Transacción finalizada")
    conexion.close()
