from usuario import Usuario
from usuarioDAO import UsuarioDAO

opcion = None

while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            print(usuario)
    elif opcion == 2:
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(username=username,password=password)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        print(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario = int(input('Escribe el ID del usuario a modificar: '))
        username = input('Escribe el nuevo username: ')
        password = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario=id_usuario,username=username,password=password)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        print(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario = int(input('Escribe el ID del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        print(f'Usuarios eliminados: {usuarios_eliminados}')