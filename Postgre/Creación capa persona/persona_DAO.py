from cursorDelPool import CursorDelPool
from logger_base import log
from persona import Persona
class PersonaDAO():
    '''
    Clase que se encarga de la conexión con la base de datos y de realizar operaciones CRUD sobre la tabla persona
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
    
    @classmethod
    def insertar(cls, persona):
            with CursorDelPool() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email)
                    cursor.execute(cls._INSERTAR, valores)
                    log.debug(f'Valores insertados: {valores}')
                    return cursor.rowcount
        
    @classmethod
    def actualizar(cls, persona):
            with CursorDelPool() as cursor:

                    valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                    log.debug(f'Valores actualizados: {valores}')
                    cursor.execute(cls._ACTUALIZAR, valores)
                    return cursor.rowcount
    
    @classmethod
    def eliminar(cls, persona):
            with CursorDelPool() as cursor:
                    valores = (persona.id_persona,)
                    log.debug(f'Valores eliminados: {valores}')
                    cursor.execute(cls._ELIMINAR, valores)
                    return cursor.rowcount
    
if __name__ == '__main__':

    # Insertar un registro
    persona = Persona(nombre='Carlos', apellido='Lara',email= 'Clara@gmail.com')
    registros_insertados = PersonaDAO.insertar(persona)
    print(f'Registros insertados: {registros_insertados}')

    # Actualizar un registro
    persona = Persona(id_persona=1, nombre='Juan', apellido='Pérez',email='123@gmail.com')
    registros_actualizados = PersonaDAO.actualizar(persona)
    print(f'Registros actualizados: {registros_actualizados}')
    
    # Eliminar un registro
    persona = Persona(id_persona=2)
    registros_eliminados = PersonaDAO.eliminar(persona)
    print(f'Registros eliminados: {registros_eliminados}')
    
    # Seleccionar registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        print(persona)
    print('Registros seleccionados: ', len(personas))