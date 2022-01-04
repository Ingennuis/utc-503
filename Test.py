#!/bin/python3
import os, shutil, sys
from time import sleep


yes_answer=["o", "y", "oui", "yes"]
space_to=['-', '_', '']
rep_sort_name=['Images', 'Videos', 'Documents', 'Musiques']
ext_image=['jpeg', 'png', 'jpg', 'gif', 'tiff']
ext_video=['avi', 'mpg', 'mp4', 'wmv', 'mov', 'flv']
def clean():
    os.system('clear' if os.name =='posix' else 'cls')
        
def msg_print(text): #Affiche un message comme s il etait tape
    for char in text:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
        
def msg_print_error(text, time): #Affiche un message en rouge clignotant
    for i in range(int(time)):
        clean()
        sleep(0.3)
        sys.stdout.write(f'\r\033[91m{text}\033[0m')
        sleep(0.3)

def msg_print_exec(text):
    sys.stdout.write(f'\033[92m')
    msg_print(text)
    print(f'\033[0m')
    sleep(0.5)

def print_indir(): #Affiche le contenu du dossier actif.
    location=os.getcwd()
    print(f'Contenu du dossier : \033[92m{location}\033[0m') #affiche en vert
    directory = os.listdir(location)
    for file in directory :
        msg_print(file)
        print('')
    sleep(1)
        
def ask_dir(): #Demande et rend actif le repertoire
    place=os.getcwd()
    print(f'Votre position :{place}')
    msg_print('Voulez-vous changer de répertoire [O/N] ?')
    choix_rep=str(input(''))
    
    if choix_rep.lower() in yes_answer:
        location = str(input("\rSpécifiez le répertoire voulu :"))
    else :
        location=str(os.getcwd())
    #test si le repertoire est bon
    try :
        os.chdir(location)
    except : #si erreur, affiche erreur et prend le repertoire actuel
        msg_print_error('Pas de répertoire choisie, ou erreur !', '5')
        location=str(os.getcwd())
        os.chdir(location)
    
    clean()
    print(f"Répertoire actif : \033[92m{location} \033[0m ") #Affiche en vert.
    return location

def replace_space(name, replace_caracter):
    name = name.strip()
    name = name.replace(' ', replace_caracter)
    return name

def replace_extension(name, ext_to_replace, replace_caracter):
    if not "." in ext_to_replace :
        ext_to_replace= "."+ ext_to_replace
    if not "." in replace_caracter :
        replace_caracter= "."+ replace_caracter
    new_name = name.replace(ext_to_replace, replace_caracter)
    return new_name


def rename_file(directory) : #Fonction de renommage, inclu les questions
    msg_print('Voulez-vous remplacer les extensions de fichier [O/N] ?')
    choix_rep_ext=str(input())
    if choix_rep_ext.lower() in yes_answer:
        ext_to_replace=str(input("Extension à remplacer : "))
        replace_caracter=str(input("Remplacer par :"))
    else:
        ext_to_replace=''
        replace_caracter=''
    clean()
    msg_print("Voulez-vous remplacer les espaces dans les noms de fichier [O/N] ?")
    choix_rep_space=str(input())
    if choix_rep_space.lower() in yes_answer :
        check=False
        while check==False:
            try : #Casse si l'input n'est pas un chiffre
                clean()
                number_caracter=int(input(f'Remplacer les espaces dans les noms par : \n \t1: -\n\t2: _\n\t3: Rien \n Faites votre choix, tapez 1, 2 ou 3 (lettre :quit):'))-1
                if number_caracter in range(3):
                    check=True
                else :
                    msg_print_error(" Veuillez entrez 1, 2 ou 3 !", '5')
                    check=False
            except :
                print('Annulé')
                quit()
                
    clean()
    msg_print_exec('OK ...')
    for file in directory : #Execute les actions demandees
        if (choix_rep_ext.lower() in yes_answer and choix_rep_space.lower() in yes_answer) and (' 'in file and ext_to_replace in file) :
                file_new_name = str(replace_extension(file, ext_to_replace, replace_caracter))
                file_last_name = str(replace_space(file_new_name, space_to[number_caracter]))
                os.rename(file, file_last_name)
                msg_print(f'{file} --> {file_new_name} --> {file_last_name}\n')
        else :
            if ext_to_replace in file and choix_rep_ext.lower() in yes_answer :
                file_new_name = str(replace_extension(file, ext_to_replace, replace_caracter))
                os.rename(file, file_new_name)
                msg_print(f'{file} --> {file_new_name}\n')
            if choix_rep_space.lower() in yes_answer and ' ' in file :
                file_new_name = str(replace_space(file, space_to[number_caracter]))
                os.rename(file, file_new_name)
                msg_print(f'{file} --> {file_new_name}\n')

def sort_by_ext(): #Fonction qui déplace les fichiers dans les bons répertoires
    location=os.getcwd()
    directory = os.listdir(location)
    print_indir()
    msg_print('Trier les fichiers et créer des dossiers de rangement dans ce rerpetoire : ')
    msg_print_exec(location)
    msg_print('Garder ce répertoire de destination [O/N] ?')
    choix_rep_dest=str(input())
    if choix_rep_dest.lower() in yes_answer:
        rep_dest=location
    else :
        check = False
        while check == False:
            msg_print('Entrez le repertoire de destination :')
            rep_dest=str(input())
            if os.path.isdir(rep_dest) == True:
                check = True
            else:
                msg_print_error("Le repertoire que vous avez rentré n'est pas valide !", "7")
                clean()
                check= False
    slash=('/' if os.name =='posix' else '\\')
 
    if not rep_dest[:-1].endswith('\\') or not rep_dest[:-1].endswith('/'): #verfie que la destination comporte bien un slash ou un antislash (l ajoute si besoin)
        rep_dest= rep_dest +  slash

    msg_print_exec('ok ...')
    for rep_name in rep_sort_name: #Creer les repertoires de trie s il n existe pas.
        if not os.path.exists(rep_dest+rep_name):
            os.makedirs(rep_dest+rep_name)
            msg_print(f'create : {rep_dest}{rep_name}\n')
            
            
    for file in directory:
        ext = extension(file)
        if ext in ext_image :
            shutil.move(location+slash+file, rep_dest+rep_sort_name[0]+slash+file)
            msg_print(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[0]}{slash}{file}\n')
        if ext in ext_video :
            shutil.move(location+slash+file, rep_dest+rep_sort_name[1]+slash+file)
            msg_print(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[1]}{slash}{file}\n')
        
    
            
def extension(name):
    ext='.'.join(name.split('.')[1:])
    ext = ext if ext else None
    return ext
    

#---main---
clean()#On passe un coup de balai

msg_print('Bienvenue !\n')#On dit bonjour, parcequ'on est poli

directory = os.listdir(ask_dir()) #On prend les fichiers du repertoire

msg_print("Voulez-vous renommer des noms de fichiers [O/N] ? ")
choix_rep_rename=str(input())
clean()
if choix_rep_rename.lower() in yes_answer:
    print_indir()
    rename_file(directory)
#else :
    #msg_print('Bonne journée !\n')
msg_print("Voulez trier vos fichier dans des dossiers (ex: *.png --> images/*.png) [O/N] ?")
choix_rep_sort=str(input())
clean()
if choix_rep_sort.lower() in yes_answer:
    sort_by_ext()