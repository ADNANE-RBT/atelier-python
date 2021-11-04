# fonction pour creer et remplir la nouvelle liste
def new_list (listA, listB):
    N_list = []
#2 boucles for pour prendre les valeurs necesssaire de chaque liste et les ajout dans la nouvelle liste
    for i in range (1, len(listA), 2):
            N_list.append(listA[i])
    for j in range( 0, len(listB), 2):
            N_list.append(listB[j])
    print(N_list)


list1= [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
new_list(list1,list2)