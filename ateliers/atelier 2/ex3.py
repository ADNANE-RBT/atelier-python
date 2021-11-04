#fonction pour itérer une liste donnée et compter l'occurrence de chaque élément
def iterer(list):
    my_dict={}
#boucle for pour iterer la fonction

    for i in range(len(list)):
        if list[i] in my_dict:
            my_dict[list[i]]+= 1
        else:
            my_dict[list[i]]= 1
        
    print(my_dict)

'''boucle if pour tester et calculer le nombre
doccurence de chaque variable, ou bien de creer un nouvel key dans le dictionner si
il nexiste pas deja'''


list1= [11, 45, 8, 11, 23, 45, 23, 45, 89]
iterer(list1)