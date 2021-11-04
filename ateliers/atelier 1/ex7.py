#fonction qui inverse les lettres d’une chaîne de caractères en utilisant fct reversed
def inverse(list2):
    newList = list (reversed(list2))
    print(newList)
   
    
str1 = str(input("entrer la phrase a inverser:\n"))
print("voici votre phrase avant l'inverser:\n",str1)

#pour inverser le str, j'ai decide de le positionner dans une list, puis inverser la liste
n= len(str1)
list1=[]
#boucle for pour remplir la liste, puis linverser dans la fonction "inverse"
for i in range(0,n):
        list1.append(str1[i])
print(list1)

print(inverse(list1))



