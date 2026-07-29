# 1 .crre un algo qui genere des nombres au hasard
# 2.Tant que l'utilisatuer n'a pas trouve le bon nombre 
# 2.1. Demander un nombre a l'utilisateur 
# 2.2. Si le nombre est trop petit on vas affiche le message "c'est plus "
# 2.3. Si le nombre est plus grand on vas affiche le message "c'est moin "
# 3. Quand il vas trouver le bon nombre on vas le felicite part le message "barvos vous avez trouver le nombre jsute "
import random

nb  = random.randint(1 , 600)
saisis = -1 
abandone = False
while saisis != nb:
    instruction = input("veuillez entre un nombre entre 1 et 600 [q : Quitte ] ") 

    if not instruction.isnumeric():
        if instruction == 'q':
            abandone = True 
            break 
        else:
           print("la saisie entre n'ets pas valide ")
    
    saisis = int(instruction)
    if saisis < nb : 
        print("C'est plus ")
    elif saisis > nb :
        print("c'est moin ")
if abandone:
  print(f"Dommage le nombre etais {nb}")
else:
  print(f"Bravos vous avez trouvez le nombre {nb}")




