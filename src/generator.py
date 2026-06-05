#Importa bibliotecas
import time

#Entrada de dados pessoais
name = input("Enter your name: ")
address = input("Enter your address: ")

#Entrada de dados empresariais
hired = input("Enter your hiring date: ")
title = input("Enter your job title: ")
division = input("Enter your role: ")

#Gerador de cartões (parte 1 = gerência)
if division == "Operational":
    part1 = "OPER"
elif division == "Developer":
    part1 = "DEV"
elif division == "Security":
    part1 = "SEC"
else:
    print("Insert valid role.")

