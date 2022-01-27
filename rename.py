#!/bin/python3
import os
import shutil
import sys
import argparse

parser = argparse.ArgumentParser()
#----Arguments----
parser.add_argument('-p', '--path', help="path to your directory", required=True, type=str)
parser.add_argument('-d', '--destination-path', help='choose a destination folder', dest='destination')
parser.add_argument('-s', '--space-replace', help='replace space by underscore or your choice', dest='space_character', nargs='?', const='_')
parser.add_argument('-o', '--order-files', help='organize files in folder acording to their type', action='store_true', dest='order')
parser.add_argument('-ext', '--ext-replace', help='replace a choosen extension file by an other Usage : -ext [ext-to-replace] [replace-ext]', nargs=2, dest='ext')
parser.add_argument('-r', '--rename', help='rename all files, file_1, file_2, ..., file_n | image_1...', action='store_true')
parser.add_argument('-v', '--verbose', help='show you what was done', action='store_true')
args = parser.parse_args()

#----Variables----
files={} #Can be better
count={'image':1, 'document':1, 'video':1, 'music':1, 'file':1 }
ext_image=['jpeg', 'png', 'jpg', 'gif', 'tiff','bmp'] #We can use a library to compare type
ext_video=['avi', 'mpg', 'mp4', 'wmv', 'mov', 'flv']
ext_music=['mp3', 'wav', 'ogg', 'wma', 'mid', 'm4a']
ext_doc=['doc', 'docx', 'txt', 'odt', 'xls', 'dot', 'dotx','xlsm', 'xlsx', 'pdf' ]
rep_sort_name=['Images', 'Videos', 'Documents', 'Musics', 'Files']


#----Functions----
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

def store_names(name): #store names in dictionary
    files[name]=name


def verbose(text): #display changes
    if args.verbose :
        print(f'{text}')

def rename(name, kind) : #rename acording to the extension file
    ext=extension(name)
    if ext :
        name=f'{kind}_{count[kind]}.{ext}'
    else:
        name=f'{kind}_{count[kind]}'
    count[kind]=count[kind]+1
    return name

def extension(name): #return file's extension
    ext='.'.join(name.split('.')[1:])
    ext = ext if ext else None
    return ext

def create_dir():
    for rep_name in rep_sort_name: #Create folder if not exist
        if not os.path.exists(rep_dest+rep_name) and count[str(rep_name[:-1].lower())] > 1:
            try:
                os.makedirs(rep_dest+rep_name)
                verbose(f'create : {rep_dest}{rep_name}')
            except :
                print(f'\033[91mError : Impossible to create {rep_dest}{rep_name}\033[0m')
                sys.exit()

def order_files(): #order file in the right folder
    for file in files:
        ext = extension(file)
        if ext in ext_image :
            shutil.move(f'{location}{slash}{file}', f'{rep_dest}{rep_sort_name[0]}{slash}{file}')
            verbose(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[0]}{slash}{file}')
        elif ext in ext_video :
            shutil.move(f'{location}{slash}{file}', f'{rep_dest}{rep_sort_name[1]}{slash}{file}')
            verbose(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[1]}{slash}{file}')
        elif ext in ext_doc :
            shutil.move(f'{location}{slash}{file}', f'{rep_dest}{rep_sort_name[2]}{slash}{file}')
            verbose(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[2]}{slash}{file}')
        elif ext in ext_music :
            shutil.move(f'{location}{slash}{file}', f'{rep_dest}{rep_sort_name[3]}{slash}{file}')
            verbose(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[3]}{slash}{file}')
        else:
            shutil.move(f'{location}{slash}{file}', f'{rep_dest}{rep_sort_name[4]}{slash}{file}')
            verbose(f'{location}{slash}{file} move to --> {rep_dest}{rep_sort_name[4]}{slash}{file}')

def files_types(ext) : #return file type acording to their extension
    if ext in ext_image:
        kind='image'
    elif ext in ext_doc:
        kind='document'
    elif ext in ext_video:
        kind='video'
    elif ext in ext_music:
        kind='music'
    else:
        kind='file'
    return kind



#----Main----
os.chdir(args.path)
location=os.getcwd()
directory=os.listdir(location)

if args.destination: #define destination folder
    destination=args.destination
    if not os.path.isdir(destination) :
        print('\033[91mError : Wrong destination ! Not Folder\033[0m')
        sys.exit()
else:
    destination=os.getcwd()
slash=('/' if os.name =='posix' else '\\')
if not destination[-1]=='\\' and not destination[-1]=='/':#verify if the the destination have a skash in the end, then add it
    rep_dest= destination +  slash
else:
    rep_dest=destination
for file in directory : #take files to put it in  into dictionary
    if os.path.isfile(file) :
        store_names(file)
if args.space_character :
    for file in files:
        files[file]=replace_space(files[file], args.space_character) #change the futur name of the file : files[actual_name]=futur_name
if args.ext :
    for file in files :
        files[file]=replace_extension(files[file], args.ext[0], args.ext[1])
if args.rename : #rename acording to extension file
    for file in files:
        files[file]=rename(files[file], files_types(extension(file)))

#***Make the changes in the files names***
for file in files : #prompt names changes and makes changes
    if files[file] not in file: #see if the names was changed, and make changes
        if args.order : #if order no need to move file now.
            try :
                os.rename(file, files[file])
                verbose(f'rename : {file} --> {files[file]}')
            except :
                print(f'\033[91mError : Impossible to change {file} --> {files[file]}\033[0m')
                sys.exit()
        else :
            try :
                shutil.move(f'{location}{slash}{file}', f'{rep_dest}{files[file]}')
                verbose(f'rename and move : {location}{slash}{file} --> {rep_dest}{files[file]}')
            except :
                print(f'\033[91mError : Impossible to change or move {location}{slash}{file} --> {rep_dest}{files[file]}\033[0m')
                sys.exit()
#***Make the changes in the files names*** Can be put in a function...

if args.order :
    files={}
    directory=os.listdir(location)
    for file in directory : #take files to put it in  into dictionary
        if os.path.isfile(file) :
            store_names(file)
    verbose('\n')
    if not args.rename: #count each type of file, to do not create useless folder
        for file in files:
            ext=extension(file)
            count[files_types(ext)]=count[files_types(ext)]+1
    create_dir()
    order_files()
print('\033[92mDone !\033[0m')

#count can improve for display statistics
