#Importa bibliotecas
import time

#Entrada de dados pessoais
name = input("Enter your name: ")
address = input("Enter your address: ")

#Entrada de dados empresariais
while True:
    try:
        hired = int(input("Enter your hiring date (DD/MM/YYYY): "))
        break
    except ValueError:
        print("Only numbers!")

title = input("Enter your job title: ")
division = input("Enter your role: ")

while True:
    division = input("Enter your role: ")

    if division == "Operational":
        part1 = "OPER"
        break
    elif division == "Developer":
        part1 = "DEV"
        break
    elif division == "Security":
        part1 = "SEC"
        break
    else:
        print("Insert valid role.")

#Modificador de variáveis (parte 2 = código numérico)
part2 = (str(hired)[::-1])

#Modificador de variáveis (parte 3 = código alfabético)
divide_name = name.split()
print(divide_name)

#hired = 
#print(f"{part1}-{part2}-{part3}")