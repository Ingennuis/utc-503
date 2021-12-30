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
    os.chdir(location)
    return location

def replace_space(name, replace_caracter):
    name = name.replace(' ', replace_caracter)
    return name

def replace_extension(name, ext_to_replace, replace_caracter):
    if not "." in ext_to_replace :
        ext_to_replace= "."+ ext_to_replace
    if not "." in replace_caracter :
        replace_caracter= "."+ replace_caracter
    new_name = name.replace(ext_to_replace, replace_caracter)
    return new_name


def rename_file(directory) :
    choix_rep_ext=str(input(f'Voulez-vous remplacer les extensions de fichier [O/N] ?'))
    if choix_rep_ext.lower() in yes_answer:
        ext_to_replace=str(input("Extension à remplacer : "))
        replace_caracter=str(input("Remplacer par :"))
        

    choix_rep_space=str(input(f'Voulez-vous remplacer les espaces dans les noms de fichier [O/N] ?'))
    if choix_rep_space.lower() in yes_answer :
        check=0
        while check==0:
            i=int(input(f'Remplacer les espaces dans les noms par : \n \t1: -\n\t2: _\n\t3: Rien \n Faites votre choix, tapez 1, 2 ou 3 :'))-1
            if i in range(3):
                check=1
            else :
                print(f"\033[91m Veuillez entrez 1, 2 ou 3 \033[0m")
                check=0

    for file in directory :
        if ext_to_replace in file and choix_rep_ext in yes_answer :
            file_new_name = str(replace_extension(file, ext_to_replace, replace_caracter))
            os.rename(file, file_new_name)
            print(f'{file} --> {file_new_name}')
        if choix_rep_space in yes_answer and ' ' in file:
            file_new_name = str(replace_space(file, space_to[i]))
            os.rename(file, file_new_name)
            print(f'{file} --> {file_new_name}')

print(f'Bienvenue :')
directory = os.listdir(ask_dir())

choix_rep_rename=str(input(f'Voulez-vous changer les noms des fichier du répertoire [O/N] ?'))
if choix_rep_rename in yes_answer:
    print('\r')
    rename_file(directory)
else :
    print(f'Bonne journée')