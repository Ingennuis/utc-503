#!/bin/python3
import os, shutil, sys
import argparse

parser = argparse.ArgumentParser()
#Declare arguments and options
parser.add_argument('-p', '--path', help="path to your directory", required=True, type=str)
parser.add_argument('-d', '--destination-path', help='choose a destination folder')
parser.add_argument('-s', '--space-replace', help='replace space by underscore or your choice', dest='space_character', nargs='?', const='_')
parser.add_argument('-o', '--order-files', help='organize files in folder acording to their type', action='store_true')
parser.add_argument('-ext', '--ext-replace', help='replace a choosen extension file by an other Usage : -ext [ext-to-replace] [replace-ext]', nargs=2, dest='ext')
parser.add_argument('-r', '-rename', help='rename all files, file_1, file_2, ..., file_n', action='store_true')
parser.add_argument('-z', '--zip', help='compress all output in zip folder', action='store_true')
parser.add_argument('-v', '--verbose', help='show you what was done', action='store_true')
args = parser.parse_args()

files={}

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


def verbose(text):
    if args.verbose :
        print(f'{text}')


#main
location=os.chdir(args.path)
directory=os.listdir(location)
for file in directory :
    if os.path.isfile(file) :
        store_names(file)
if args.space_character :
    for file in files:
        files[file]=replace_space(files[file], args.space_character) #change the futur name of the file : files[actual_name]=futur_name
if args.ext :
    for file in files :
        files[file]=replace_extension(files[file], args.ext[0], args.ext[1])
if args.rename :
    #to do