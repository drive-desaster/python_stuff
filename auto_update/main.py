#!/bin/python3


import os
#import git
import shutil

#'config' file
file = open("pks",'r')

for package in file.readlines() :
    package = package.replace('\n', '')
    print(f"package: {package}")
    os.system(f"git clone https://aur.archlinux.org/{package}.git")
    os.chdir(package)
    print(f"Building {package}")
    os.system("makepkg")
    
    print("copying filtes to pkg dir")
    for pkg in os.listdir() :
        if ".tar.zst" in pkg :      #fertiges packet aus ordner kopieren
            shutil.copyfile(pkg, f"../pkg/{pkg}")
            
    print("removing" + package + "files")
    os.chdir("..")
    shutil.rmtree(package)   #dateinen löschen
file.close()
