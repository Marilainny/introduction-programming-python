print("Paramentro end=' ' não permite criar uma nova linha")
#imprimir sobrescrever o vaor padrão não permitindo escreve nova linha
name = input("Qual é o seu nome? ")
print("Hello, ", end="")
print(name)

print("formatar strings")
print(f"Hello, {name}")

#Remover espaço
name = name.strip()

#Colocar a primeira letra maiuscula
name = name.title()

#Simplificando o código
name = name.strip().title()

print("Remover espaço e Colocar a primeira letra maiuscula")
name = input("Qual é o seu nome e sobrenome? ").strip().title()
first, last = name.split(" ")
print("Hello,", first, last)
