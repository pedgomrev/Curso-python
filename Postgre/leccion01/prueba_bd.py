import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(
                            user = 'postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'Test_db'
                        )

#cursor
cursor = conexion.cursor()

# Sentencia SQL

sql = 'SELECT * FROM persona'
cursor.execute(sql)
personas = cursor.fetchall()
print(personas)
cursor.close()
conexion.close()