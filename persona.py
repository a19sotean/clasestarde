class Persona:

    def __init__(self, sexo, nombre, estatura, edad, peso, color_piel, color_pelo, tiene_pelo, color_ojos, tiene_gafas):
        self.sexo = sexo
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
        self.peso = peso
        self.color_piel = color_piel
        self.color_pelo = color_pelo
        self.tiene_pelo = tiene_pelo
        self.color_ojos = color_ojos
        self.tiene_gafas = tiene_gafas

    def cumplir_anos(self):
        self.edad = self.edad + 1
        return self.edad

    def comer(self, comida):
        print("Estoy comiendo " + comida)

    def dormir(self):
        print("Estoy durmiendo")

    def despertar(self):
        print("Estoy despierto")

    def andar(self, direccion, tiempo=0, distancia=0):
        if tiempo == 0:
            print("Anda " + distancia + " Km dirección " + direccion)
        elif distancia == 0:
            print("Anda " + tiempo + " min dirección" + direccion)