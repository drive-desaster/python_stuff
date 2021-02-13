text = input("zu verschlüssender text(in Großbuchstaben! ohne leerzeichen,symbole oder zahlen): ").upper().replace(' ','')
key =  int(input("Schlüssel(zahl): "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"   #alphabet als referenzwert


out = ""    #variablen erstellen
#print(F"{key=}")
for i in range(len(text)) :
    out += alphabet[alphabet.find(text[i])+key]
    #print(F"{i=} ; {out=} ; {alphabet.find(text[i])+key}")
print(out)
