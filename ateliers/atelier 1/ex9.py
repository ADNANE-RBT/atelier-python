#une fonction qui cherche un élément dans une matrice puis renvoi sa position « i,j »
def position_nombre(l, char):
    lig=0
    col=0
#2 boucles for pour trouver la position, du ligne first, apres la cologne
    for i in range(len(l)) :
       
        for j in range(len(l[i])):
#copier la position si elle est egale
            if( l[i][j]== char):
                lig= i
                col=j
                print("la position de  ", char, "est", (lig, col))


lst=[[1,2,3],[3,5,6],[7,8,9]]
char=int(input("entrer le caracter a chercher son position:\n"))
position_nombre(lst, char)

