#methode 2 sans utiliser la fonction counter
def nombre_occurence(l, char):
#boucle for pour tester chaque character de la phrase puis incrementer si c'est vrais et returner n
    n=0
    for i in l:
        if( i == char):
            n=n+1
    return n

str1 = str(input("entrer votre phrase:\n"))
char=(input("entrer le caracter a chercher son nombre d'occurence:\n"))

print("le nombre d'occurence de ", char, "est", nombre_occurence(str1, char))