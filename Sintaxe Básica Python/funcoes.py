#Função é um bloco de código, que possui um identificador, dados de entrada e dados de saída, em Python uma função é representada pela palavra reservada def. Ex:

def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Olá, seja bem vindo {nome}!')

def exibir_mensagem_3(nome='Anônimo'):
    print(f'Olá, Seja bem vindo {nome}!')


#Chamando as Funções

exibir_mensagem()
exibir_mensagem_2(nome='Luiz')
exibir_mensagem_3()
exibir_mensagem_3('Eduardo')