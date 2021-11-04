# Programme principale pour tester les 3 codes ci-dessus
#on declare le tableau si dessou pour le trier
from array import*
tab =([98, 22, 15, 32, 2, 74, 63, 70, 34, 45, 754, 1235])

# Programme Python pour faire du Tri à bulle
def tri_bulle(T):
    n=len(T)
    tri=True
    while tri == True:
        tri=False
        for i in range(0, n-1):
            
            if T[i] >=  T[i+1] :
                tmp = T[i]
                T[i]= T[i+1]
                T[i+1]=tmp
                tri= True
        n=n-1

print("le tableau avant le tri a bulle:\n\n", tab)
print("---------------------------------------------------------------------------------\n\n")
tri_bulle(tab)
print ("Le tableau apres le tri a bulle est:\n\n", tab)


# reinsitialisation des valeur du tableau:
tab = [98, 22, 15, 32, 2, 74, 63, 70, 34, 45, 754, 1235]


# Programme Python pour faire du Tri par selection :

def tri_selct(T):
    for i in range(0, len(T)-1):
        min= T[i]
        val_min= i
        for j in range(i+1, len(T)):
            if T[j]< min:
                min = T[j]
                val_min=j
        tmp= T[i]
        T[i]=T[val_min]
        T[val_min] = tmp


print("*************************************************************\n\n")
print("le tableau avant le tri par selction:\n\n", tab)
print("---------------------------------------------------------------------------------\n\n")
tri_selct(tab)
print("le tableau apres le tri par selection est :\n\n", tab)



# reinsitialisation des valeur du tableau:
tab = [98, 22, 15, 32, 2, 74, 63, 70, 34, 45, 754, 1235]

# Programme Python pour faire du Tri par insertion:
def tri_inser(T):
    for i in range (1, len(T)):
        tmp = T[i]
        j= i-1
        while j>=0 and T[j]> tmp:
            T[j+1] = T[j]
            j= j-1
        T[j+1] = tmp

print("*************************************************************\n")
print("le tableau avant le tri par insertion:\n\n", tab)
print("---------------------------------------------------------------------------------\n\n")
tri_inser(tab)
print("le tableau apres le tri par insertion est :\n\n", tab)