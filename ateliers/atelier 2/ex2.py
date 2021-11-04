#fonction pour deiviser une lsite en 3 morceau egaux
def divise_inverse(listA):
# division de la liste sur 3, en assurant que n soit interger pour lutiliser apres
    n= len(listA)
    n=int(n/3)
#declaration de la 1ere nouvelle liste et la remplir par les valeurs de la listeA de 0 a n
    list1=[]
    list1= listA[0:n]
    list1.reverse()
    print(list1)
#declaration de la 2eme nouvelle liste et la remplir par les valeurs de la listeA de n a -n "equivalent a 2n"
    list2=[]
    list2= listA[n:-n]
    list2.reverse()
    print(list2)
#declaration de la 3eme nouvelle liste et la remplir par les valeurs de la listeA de -n a la fin de la list
    list3=[]
    list3= listA[-n:]
    list3.reverse()
    print(list3)
   
list_a= [11, 45, 8, 23, 14, 12, 78, 45, 89,45,34,56]
divise_inverse(list_a)