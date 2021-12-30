#!/bin/python3
import os

yes_answer=["o", "y", "oui", "yes"]
space_to=['-', '_', '']


def ask_dir():
    place=os.getcwd()
    choix_rep=str(input(f'Votre position :{place}\n Voulez-vous changer de répertoire [O/N] ?'))
    if choix_rep.lower() in yes_answer:
        location = str(input("Spécifiez le répertoire voulu :"))
    else :
        location=os.getcwd()
    return location

def replace_space(name, replace_caracter):
    name = name.replace(' ', replace_caracter)
    return name

name=str(input('name :'))
i=str(input(f'Remplacer les espaces dans les noms par : \n'for signe in space_to[]:'{signe}\n'))

print(replace_space(name, space_to[i]))
