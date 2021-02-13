#!/bin/python3
text = input("verschlüssender text(in Großbuchstaben! ohne leerzeichen,symbole oder zahlen): ").upper().replace(' ', '')
key =  int(input("Schlüssel(zahl): "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"   #alphabet als referenzwert


i = 0
out = ""    #variablen erstellen
#print(F"{key=}")
for i in range(len(text)) :
    out += alphabet[alphabet.find(text[i])-key]
    #print(F"{i=} ; {out=}")
    i += 1
print(out)
