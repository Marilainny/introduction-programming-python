#Declarar variavél
x = 1
y = 2

z = x + y
print(z)

# Input
x = input("Qual é o valor de x? ")
y = input("Qual é o valor de y? ")

z = int(x) + int(y)
print(z)

#Simplificando o código
x = int(input("Qual e o valor de x? "))
y = int(input("Qual e o valor de y? "))

z = (x + y)
print(z)

#Float
x = float(input("Qual é o valor de x? "))
y = float(input("Qual é o valor de y? "))

z = round(x + y)

#formatar o resultado
print(f"{z:,}")

z = x / y
print(f"{z:.2f}")
