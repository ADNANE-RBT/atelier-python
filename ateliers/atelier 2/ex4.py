#fonction permet deTrouver l'intersection de 2 Sets et supprimez ces éléments du 1ere Set

def inter( listA, listB):
#creer un nouveau dictionnaire pour filtrer le contenu des listes
    intersection= {n for n in listA if n in listB}
    print( "lintersection de notre 2 listes est : \n",intersection)
#supprimer ces element de la 1ere liste
    listA= { n for n in listA if n not in listB }
    print("la nouvelle liste est: \n",listA)

list1=[23, 42, 65, 57, 78, 83, 29]
list2= [57, 83, 29, 67, 73, 43, 48]
inter(list1,list2)