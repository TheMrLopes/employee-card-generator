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
    try:
        if division == "Operational":
            part1 = "OPER"
        elif division == "Developer":
            part1 = "DEV"
        elif division == "Security":
            part1 = "SEC"
    except:
        print("Insert valid role.")
    break

#Gerador de cartões (parte 1 = gerência)


part2 = (str(hired)[::-1])

#hired = 
print(f"{part1}-{part2}")