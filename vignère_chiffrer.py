text = input("zu verschlüssender text(in Großbuchstaben! ohne leerzeichen,symbole oder zahlen): ").upper()
key =  input("Schlüssel(ohne leerzeichen,symbole oder zahlen! In Großbuchstaben!): ").upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   #alphabet als referenzwert
matrix = [
    ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
    ["BCDEFGHIJKLMNOPQRSTUVWXYZA"],
    ["CDEFGHIJKLMNOPQRSTUVWXYZAB"],
    ["DEFGHIJKLMNOPQRSTUVWXYZABC"],
    ["EFGHIJKLMNOPQRSTUVWXYZABCD"],
    ["FGHIJKLMNOPQRSTUVWXYZABCEF"],
    ["GHIJKLMNOPQRSTUVWXYZABCDEF"],
    ["HIJKLMNOPQRSTUVWXYZABCDEFG"],
    ["IJKLMNOPQRSTUVWXYZABCDEFGH"],
    ["JKLMNOPQRSTUVWXYZABCDEFGHI"],
    ["KLMNOPQRSTUVWXYZABCDEFGHIJ"],
    ["LMNOPQRSTUVWXYZABCDEFGHIJK"],         #matrix(vinére tabelle) erstellen
    ["MNOPQRSTUVWXYZABCDEFGHIJKL"],
    ["NOPQRSTUVWXYZABCDEFGHIJKLM"],
    ["OPQRSTUVWXYZABCDEFGHIJKLMN"],
    ["PQRSTUVWXYZABCDEFGHIJKLMNO"],
    ["QRSTUVWXYZABCDEFGHIJKLMNOP"],
    ["RSTUVWXYZABCDEFGHIJKLMNOPQ"],
    ["STUVWXYZABCDEFGHIJKLMNOPQR"],
    ["TUVWXYZABCDEFGHIJKLMNOPQRS"],
    ["UVWXYZABCDEFGHIJKLMNOPQRST"],
    ["VWXYZABCDEFGHIJKLMNOPQRSTU"],
    ["WXYZABCDEFGHIJKLMNOPQRSTUV"],
    ["XYZABCDEFGHIJKLMNOPQRSTUVW"],
    ["YZABCDEFGHIJKLMNOPQRSTUVWX"],
    ["ZABCDEFGHIJKLMNOPQRSTUVWXY"]
    ]

while (len(text) > len(key)) :      #schlüssel auf lange des textes bringen
    key += key

i = 0
out = ""    #variablen erstellen
#print(F"{key=}")
while i != len(text) :
    out += matrix[alphabet.index(key[i])][0][alphabet.index(text[i])]
    #print(F"{i=} ; {out=}")
    i += 1
print(out)
