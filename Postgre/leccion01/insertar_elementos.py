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
                # Sentencia SQL
                sql = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
                # Valores a insertar
                nombre = input("Proporciona el nombre: ")
                apellido = input("Proporciona el apellido: ")
                email = input("Proporciona el email: ")
                valores = (nombre, apellido, email)
                cursor.execute(sql, valores)
                # Guardamos la información en la base de datos
                registros_insertados = cursor.rowcount                
                print(f"Registros insertados: {registros_insertados}")
                sql = 'SELECT * FROM persona where nombre = %s'
                cursor.execute(sql, (nombre,))
                registros = cursor.fetchone()
                '''
                Código para insertar varios registros
                
                print(registros)
                valores = (
                    ('Carlos','Gonzalez','cg@gmail.com'),
                    ('Karla','Ramirez','kr@gmail.com'),
                    ('Manuel','Gutierrez','mg@gmail.com')
                )
                cursor.executemany(sql, valores)
                registros_insertados = cursor.rowcount
                print(f"Registros insertados: {registros_insertados}")
                '''
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()