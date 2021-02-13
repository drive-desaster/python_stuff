#!/bin/python3.9

import random
#zufals-zahl(0-2)wählen
print("\n\n\n")
legende = ["Stein","Schere","Papier"]
comp = random.randint(0,2)


##in diesen abschnitt legt der nutzer seine wahl fest.##
repeat = True
while repeat :
    player = input("Bitte wählen Stein, Schere oder  papier: ")
    if player.upper() == "STEIN" :
        player = 0
        repeat = False
    elif player.upper() == "SCHERE" :
        player = 1
        repeat = False
    elif player.upper() == "PAPIER" :
        player = 2
        repeat = False
    else :
        print(f"you donkey, {player} stand nicht zur wahl! try again.")
#       sie haben mir erlaubt, den spieler zu beleidigen!
##END OF SEGMENT##

#an dieser stele wird auf ein unentschieden geprüft.
if player == comp :
    print("unentschieden")
    winner  = "none" 
    #
    #
## sollt es kein unentschieden sein, so wird in diesen segment der spiel ausgang festlegen.##
elif player ==0 :
    if comp == 1 :
        winner = "pl"
    else :
        winner ="comp"
elif player == 1 :
    if comp == 2 :
        winner = "pl"
    else :
        winner ="comp"
elif player == 2 :
    if comp == 0 :
        winner = "pl"
    else :
        winner ="comp"
else :
    print(f"you donkey, {player} stand nicht zur wahl")
    #altlast für den fall der fälle, das i'was schief ging
##END OF SEGMENT##
    
    
    
#       zusammenfassung
print(F"\ndie wahlen stehen fest: \nder Comuter nimmt {legende[comp]} \nund der Herrausforderer nimmt {legende[player]} .\n")

##in deisem segment wird der gewinner verkündet.##
if winner == "none" :
    print("es kan zu einem unentschieden")
elif winner == "pl" : 
    print(f"du hast den Computer mit {legende[player]} vernichtend geschlagen!")
elif winner == "comp" :
    print(f"{legende[player]} konnte den Computer leider nich besiegen!")
##END OF SEGMENT##



##altlasten
#
#if comp == 0 : #wenn 0, dann stein
#    print("Stein ist die waffe der Wahl")
#elif comp == 1 : #wenn 1 dan papier
#    print("Papier ist die waffe der Wahl")
#else :           #wenn 2 dann schere
#    print("Schere ist die waffe der Wahl")
