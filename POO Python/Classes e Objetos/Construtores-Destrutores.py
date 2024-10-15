#---------Construtor---------

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print(f'Inicializando a Classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

#---------Destrutor---------
    def __del__(self):
        print(f'Removendo a instância da classe...')

    def falar(self):        
        print(f'auau')

def criar_cachorro():
    c = Cachorro('Zeus', 'Branco e preto', False)
    print(c.nome)

c = Cachorro('Chappie', 'Amarelo')
c.falar()

print(f'Olá Mundo')
print(f'Olá Mundo')

del c

print(f'Olá Mundo')
print(f'Olá Mundo')
print(f'Olá Mundo')
print(f'Olá Mundo')

# criar_cachorro()