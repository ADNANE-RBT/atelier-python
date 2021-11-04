#fonction pour compter les chiffres d'un nombre donné en utilisant la récursivité
#si le nombre est <10 alors il est directement a 1 chiffre
#sinn on declare 1 puis l'ajout aux autre fonctions de recursivite
def calcul(x):
    if x<10:
        return 1
    else:
        return(1 + calcul(x//10))

n=int(input("give ne a number\n"))
print("voici le nombre des chiffres\n", calcul(n ))