class Personaje:

    #Constructor - Método/Función especial encargada de inicializar los atributos de mi clase.
    def __init__(self,name,type,house):

        #Creamos los atributos de la clase.
        #Atributos = Datos = Variables.
        self.name = name
        self.type = type
        self.house = house


    #Declaro los métodos o funciones de mi clase.

    def saludar(self):
        print("Hola Valen, cómo estás? :3 ")      
