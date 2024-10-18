# na herança simples a classe A herda apenas da classe B

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f'Ligando motor...')
    pass

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    #Sobrescrevendo o compotamento da classe pai
    def __init__(self, cor, placa, numero_rodas, carregado): 
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def estar_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")
    pass

moto =  Motocicleta("Preta", "abc-1234", "2")
carro = Carro("Branco", "xme-9083", "4")
caminhao = Caminhao("Cinza", "xyz-7890", "8", True)
caminhao.ligar_motor()
caminhao.estar_carregado()

print(moto)
print(carro)
print(caminhao)