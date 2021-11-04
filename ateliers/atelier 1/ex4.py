#fonction pour calculer la serie fibonacci en utilisant la recursivite
# 0 et 1 sont des cas particulier a declare, sinn on continue par recursivite
def fibonn(n):
    if n==0:
       return 0
    elif n==1:
        return 1
    else:
        return( fibonn(n-1) + fibonn(n-2))


var = int(input("donner le nombre de fois \n"))
#repeter la fonction n fois et utilisant end='' pour limprimer en un ligne
for i in range (0, var):
    print(fibonn(i), end=' ')
#j'ai ajouter \n pour retourne a ligne a la fin de la boucle for
print("\n et voici votre liste fibonacci")

