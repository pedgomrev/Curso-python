from logger_base import log
from psycopg2 import pool
from conexion import Conexion


class CursorDelPool():
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        log.debug(f'Conexión obtenida del pool: {self._conexion}')
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción: {exc_val} {exc_type} {exc_tb}') 
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

    