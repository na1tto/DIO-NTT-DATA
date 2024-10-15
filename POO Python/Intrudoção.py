
#---------Exemplo de Classe em python---------
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print(f'Zzzzz...')

#---------Exemplo de Objeto em python---------

cao_01 = Cachorro('Chappie', 'Amarelo', False)
cao_02 = Cachorro('Aladim', 'Branco e Preto')

cao_01.latir()

print(cao_02.acordado)
cao_02.dormir()
print(cao_02.acordado)