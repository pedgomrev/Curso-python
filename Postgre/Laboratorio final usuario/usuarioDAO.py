from logger_base import log
from usuario import Usuario
from cursorDelPool import CursorDelPool

class UsuarioDAO:
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _UPDATE = 'UPDATE usuario SET username=%s,password=%s WHERE id_usuario= %s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug(cursor.mogrify(cls._SELECT))
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password)
            log.debug(cursor.mogrify(cls._INSERT))
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
                valores = (usuario.username,usuario.password,usuario.id_usuario)
                log.debug(cursor.mogrify(cls._UPDATE))
                cursor.execute(cls._UPDATE,valores)
                log.debug(f'Valores actualizados: {valores}')
                return cursor.rowcount
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            log.debug(cursor.mogrify(cls._DELETE))
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    usuario = Usuario(username='jose',password='1234')
    usuarios_insertados = UsuarioDAO.insertar(usuario)
    log.debug(f'Usuarios insertados: {usuarios_insertados}\n')
    # Actualizar un registro
    usuario = Usuario(id_usuario=5,username='Manuel',password='4321')
    usuarios_actualizados = UsuarioDAO.actualizar(usuario)
    log.debug(f'Usuarios actualizados: {usuarios_actualizados}\n')
    # Seleccionar registros
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
    