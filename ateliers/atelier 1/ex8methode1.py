#pour methode 1, on peut utiliser la fonction counter qui calcule le nombre d;o
from collections import Counter


#fonction pour trouver le nombre d'occurence en utilisant la fonction counter de string
def freq(char1):
    Val = Counter(str1)
    print("le nombre d'occurence de ", char, "et:", Val[char1])
 


str1 = str(input("entrer votre phrase:\n"))

char=(input("entrer le caracter a chercher son nombre d'occurence:\n"))
freq(char)

