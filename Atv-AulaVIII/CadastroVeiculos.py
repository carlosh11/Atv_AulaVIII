class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def mover(self):
        print("Veículo se movimentando")


class Carro(Veiculo):
    def mover(self):
        print("Carro andando")

    def abrir_porta(self):
        print("Porta aberta")


class Moto(Veiculo):
    def mover(self):
        print("Moto andando")

    def empinar(self):
        print("Moto empinando")


carro = Carro("Toyota", "Corolla", 2024)
moto = Moto("Honda", "CG", 2023)

carro.mover()
carro.abrir_porta()

moto.mover()
moto.empinar()