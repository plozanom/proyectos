class Animal:
    def hacer_sonidos(self):
        print("El animal hace ruidos para comunicarse")


# Gato hereda de Animal
class Gato(Animal):
    # Se sobreescribe el método
    # Si llamase un objeto de la clase hija y llamara el método hacer_sonidos, mostraría un comportamiento distinto
    # al de la clase padre, si no estoy mal, eso sería polimorfismo
    def hacer_sonidos(self):
        print("Un gato maulla")


# Esta es una función polimorfica
def hacer_sonidos_animal(animal):
    animal.hacer_sonidos()
