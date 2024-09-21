#Objetos de Primeira Classe, vamos usar esse recurso para criar uma calculadora simples!

def somar (a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir (a,b):
    return a / b

def exibir_resultado(a, b, funcao): #Através dessa função eu posso exibir o resultado de qualquer operação que eu queira realizar dentro do meu algorítimo
    resultado = funcao(a,b)
    print(f'O resultado da operação é = {resultado}')

opt = int(input(f'Defina qual operação deseja realizar: \n 1) Soma \n 2) Subtração \n 3) Multiplicação \n 4) Divisão\n '))

match opt: #'Switch-Case em Python'
    case 1:
        s1 = float(input(f'Insira o primeiro valor a ser somado \n'))
        s2 = float(input(f'Insira o segundo valor a ser somado \n '))
        exibir_resultado(s1, s2, somar)
    case 2: 
        s1 = float(input(f'Insira o primeiro valor a ser subtraído \n'))
        s2 = float(input(f'Insira o segundo valor a ser subtraído \n '))
        exibir_resultado(s1, s2, subtrair)
    case 3:
        s1 = float(input(f'Insira o primeiro valor a ser multiplicado \n'))
        s2 = float(input(f'Insira o segundo valor a ser multiplicado \n '))
        exibir_resultado(s1, s2, multiplicar)
    case 4:
        s1 = float(input(f'Insira o dividendo \n'))
        s2 = float(input(f'Insira o divisor \n '))
        exibir_resultado(s1, s2, dividir)