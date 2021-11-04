#fonction pour trouver le factoriel en utilisant la recursivite
def factoriel (x):
# 1 est un cas particulier, sinon on utilise la recursivite
    if x==1:
        return 1 
    else :
        return( x * factoriel(x-1))
#declaration des var
m=5
s=0
#boucle for pour faire la somme
for i in range(1,m+1):
    s= s + factoriel(i)/i

print(s)