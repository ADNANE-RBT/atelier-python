#fonction pour faire la convertion d'un nombre binaire en un nombre decimal
def convert(x):
#le 0 est un cas particulier
    if x==0:
        return 0
#siin, on ajout le reste de la division de x sur 2
    else:
        return ((x%2)+ (10*convert(x//2)))

# demande du nombre de l'utilisateur et l'afficher
n= int(input("donner le nombre:\n"))
print("votre nombre en binaire est : \n",convert(n))
