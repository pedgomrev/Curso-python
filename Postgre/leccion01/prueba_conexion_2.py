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
                sql = 'SELECT * FROM persona WHERE id_persona = %s'
                id_persona = input("Proporciona el id_persona: ")
                cursor.execute(sql, (id_persona,))
                persona = cursor.fetchone()
                print(persona)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()