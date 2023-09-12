class Vuelo:
    def __init__(self, id="", origen="", destino="", peso=0):
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__peso = peso
        
        
    def __str__(self):
        return(
            "Identificador: " + str(self.__id) + "\n" +
            "Origen: " + self.__origen +    "\n" +
            "Destino: " + self.__destino +  "\n" +
            "Peso: " + str(self.__peso) +   "\n" 
        )
        
# v01 = Vuelo(id="0", origen="GDL", destino="MTY", peso=20)
# print(v01)