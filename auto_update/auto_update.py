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

for package in file.readlines() :       #packete zeile für zeile lesen
    package = package.replace('\n', '') 
    
    #Überprüfen, ob das packet aktuell ist
    r = requests.get('https://aur.archlinux.org/rpc/?v=5&type=search&arg=' + package) #link: https://wiki.archlinux.org/index.php/Aurweb_RPC_interface
    res = r.json()
    version_new = res['results'][0]['Version'] 
    
    
    #wenn noch nie behandelt, datei mit version für packet erstellen und neue versin hinein schreiben
    if not os.path.isfile(".version/" + package + '.v') : 
        v = open(".version/" + package + '.v', 'w')
        v.write(version_new)
        version_old = 0 # keine Versin vorhanden resultiert in versin 0
        v.close()
    
    
    else :      #wenn versions datei vorhanden, vorhandene version lesen und neu version in datei schreiben
        v = open(".version/" + package + '.v', 'r')
        version_old = v.read()                          
        v.close()
        v = open(".version/" + package + '.v', 'w')
        v.write(version_new)
        v.close()
        
        # wenn versionen unterschiedlich
    if version_new != version_old :
        print(f"package: {package}")
        os.system(f"git clone https://aur.archlinux.org/{package}.git") #packet 'herrunterladen'
        os.chdir(package) 
        print(f"Building {package}")
        
        os.system("makepkg")    #   packet bauen
        
        print("copying filtes to pkg dir")
        for pkg in os.listdir() :
            if ".tar.zst" in pkg :      #fertiges packet aus ordner kopieren
                shutil.copyfile(pkg, f"../pkg/{pkg}")
                
        print("removing" + package + "files")
        os.chdir("..")
        shutil.rmtree(package)   #dateinen löschen
    else :
        print(f"{package} is already up to date (install from ./pkg/)") #wenn versionen gleich sind, dies ausgeben
file.close()
