#!/bin/python3


import os
#import git
import shutil
import json
import requests

if not os.path.exists('pks') :
    os.mkdir('pkg')  #ordner pkg erstellen, in diesen werden später die packete verschoben
if not os.path.exists('.version') :
    os.mkdir('.version') # gleiches, wie oben jedoch zur versionierung, um die packete nicht unnötig zu machen

#'config' file
file = open("pks",'r')

for package in file.readlines() :
    package = package.replace('\n', '')
    
    #Überprüfen, ob das packet aktuell ist
    r = requests.get('https://aur.archlinux.org/rpc/?v=5&type=search&arg=' + package)
    res = r.json()
    version_new = res['results'][0]['Version'] 
    if not os.path.isfile(".version/" + package + '.v') :
        v = open(".version/" + package + '.v', 'w')
        v.write(version_new)
        version_old = 0
        v.close()
    else :
        v = open(".version/" + package + '.v', 'r')
        version_old = v.read()
        v.close()
        v = open(".version/" + package + '.v', 'w')
        v.write(version_new)
        v.close()
    if version_new != version_old :
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
    else :
        print(f"{package} is already up to date (install from ./pkg/)")
file.close()
