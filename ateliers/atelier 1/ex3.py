#fonction pour calculer la somme en utilisant la recursivite
# si le nombre=0 on retourne 0, sinn on calcule la somme dune facons decroisante

def recursiv(x):
    if x==0:
        return 0
    else:
        return( x+ recursiv(x-1))

n= int(input("give me a number of your choice \n"))

print(recursiv(n))

