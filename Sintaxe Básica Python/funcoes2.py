def somar_total(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(somar_total([30, 15, 29, 24, 90]))
print(antecessor_sucessor(10))