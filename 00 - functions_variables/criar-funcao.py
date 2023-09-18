print("Def - criar a própria função")
def hello(valor="world"):
#espaçamento
    print("hello,", valor)

#saida usando a própria função
name = input("Qual é o seu nome? ")
hello(name)

#saida usando a função default sem passar argumentos
hello()

print("Função que inicia o programa")

def main():

    name = input("Qual é o seu nome? ")
    hello(name)

    #saida sem passar argumentos default valor
    hello()

#criar nossa própria função
def hello(valor="world"):
    print("hello,", valor)

main()

print("Retornando valor")

def main():
    x = int(input("Qual o valor de x? "))
    print("O quadrado de x é ", square(x))

def square(n):
    return n * n

main()