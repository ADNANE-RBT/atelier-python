'''Itérer une liste donnée et vérifier si un élément donné existe en tant 
que valeur de clé dans un dictionnaire. Sinon, supprimez-le de la liste
'''
def test_exictence (dict, listA):
    listB=[]
#boucle for pour tester tous les index de la liste
    for i in listA:

        if i in my_dict.values():
            listB.append(i)
    print(listB)
    
'''if: tester si les valeurs existe dans le dictionnaire
 si oui, les ajoute dans la nouvelle liste'''

list1=[47, 64, 69, 37, 76, 83, 95, 97]
my_dict= {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
print(test_exictence(my_dict, list1))


            