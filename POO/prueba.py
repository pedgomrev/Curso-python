from Persona import Persona

prueba_persona = Persona('Juan', 28)
print("creacion de objeto persona".center(50, '-'))
prueba_persona.mostrar_detalles()
print("modificacion de edad".center(50, '-'))
prueba_persona.edad = 30
prueba_persona.mostrar_detalles()
print("eliminacion de objeto persona".center(50, '-'))
del prueba_persona
print("fin de la ejecucion".center(50, '-'))