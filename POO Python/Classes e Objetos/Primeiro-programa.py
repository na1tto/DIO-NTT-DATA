#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde joão informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione seus comportamentos!

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print(f'Plim PLim')

    def parar(self):
        print(f'Parando bicicleta...')
        print(f'Bicileta parada!')

    def correr(self):
        print(f'Vrummmmm...')

#---------Concatenando as Informações da minha Bicicleta---------
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# b1 = Bicicleta('Vermelha', 'Caloi', '2022', '600')
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('Verde', 'Monark', '2000', '189')
print(b2)
b2.correr()