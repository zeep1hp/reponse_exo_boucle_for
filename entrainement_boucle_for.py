
print("*****************")

#1-Écrire une boucle for qui parcourt une liste et affiche chaque élément.

liste = ["salut", "comment", "allez", "vous"]
for i in liste:
    print(i)

print("*****************")

#2-Écrire une boucle for qui parcourt une liste de nombres et calcule leur somme.

liste = [1,2,4,9,6,14,7]
for i in liste:
    print(i)
print(f"la somme des nombres de la liste est de : {sum(liste)}")

print("*****************")
1
#3-Écrire une boucle for qui parcourt une liste de chaînes de caractères et affiche leur longueur.

liste = ["salut", "comment", "allez", "vous"]
for i in liste:
    print(f"'{i}' est dans la liste et comporte {len(i)} caracteres")

print("*****************")
#4-Écrire une boucle for qui parcourt un dictionnaire et affiche chaque clé et sa valeur correspondante.

dictionnaire = {
    'clé' : 14,
    'clé2' : "valeur"            
}
for cle, valeur in dictionnaire.items():
    print(f"la '{cle}' a pour valeur '{valeur}' dans le dictionnaire")

print("*****************")

#5-Écrire une boucle for qui parcourt un dictionnaire et calcule la somme de ses valeurs.

dictionnaire = {
    'clé' : 10,
    'clé2' : 11,           
    'clé3' : 13,         
    'clé4' : 15          
}
for valeur in dictionnaire.values():
    print(valeur)
x = sum(dictionnaire.values())
print(f"la somme des valeurs du dictionnaire est de {x}")

print("*****************")

#6-Écrire une boucle for qui parcourt un dictionnaire et affiche les clés dont les valeurs sont supérieures à 10.

dictionnaire = {
    'clé' : 9,
    'clé2' : 11,           
    'clé3' : 8,
    'clé4' : 5,
    'clé5' : 20,
    'clé6' : 12,
    'clé7' : 18,         
    'clé8' : 15          
}
for cle, valeur in dictionnaire.items():
    if valeur >= 10:
        print(f"'{cle}' a une valeur superieur a 10")

print("*****************")

#7-Écrire une boucle for qui parcourt une liste de tuples et affiche chaque élément du tuple.

liste_tuple = [(0,1,2),(3,4,5),(6,7,8),(9,10,11)]
for tuple in liste_tuple:
    print(f"{tuple}")
    for entier in tuple:
        print(entier)

print("*****************")

#8-Écrire une boucle for qui parcourt une liste de tuples et calcule la somme des deuxième éléments de chaque tuple.


liste_tuple = [(0,1,2),(3,4,5),(6,7,8),(9,11,11)]
liste_element=[]
for tuple in liste_tuple:
    liste_element.append(tuple[1])
    
print(f"la somme du deuxiemme element de chaque liste est egale a {sum(liste_element)}")

print("*****************")

#9-Écrire une boucle for qui parcourt une liste de dictionnaires et affiche la valeur associée à une clé donnée pour chaque dictionnaire.


dictionnaire = {
    'cle' : 9,
    'cle2' : 11,           
    'cle3' : 8,
    'cle4' : 5          
}
dictionnaire1 = {
    'cle5' : 9,
    'cle6' : 11,           
    'cle7' : 8         
}
liste_dictionnaire = [dictionnaire,dictionnaire1]
print(liste_dictionnaire)
demande = input("quel cle veut tu consulter\n==>")
for dico in liste_dictionnaire:
    if demande in dico:
        valeur = dico[demande]
        print(f"la clé '{demande}'a pour valeur {valeur}")

print("*****************")

#10-Écrire une boucle for qui parcourt une liste de dictionnaires et calcule la somme des valeurs associées à une clé donnée pour chaque dictionnaire.

dictionnaire = {
    'cle' : 9,
    'cle2' : 11,           
    'cle3' : 8,
    'cle4' : 5          
}
dictionnaire1 = {
    'cle5' : 9,
    'cle6' : 11,           
    'cle7' : 8         
}
liste_dictionnaire = [dictionnaire,dictionnaire1]
liste_somme = []
print(liste_dictionnaire)
def recherche():
    demande = input("quel cle veut tu consulter\n==>")
    for dico in liste_dictionnaire:
        if demande in dico:
            valeur = dico[demande]
            liste_somme.append(valeur)

for i in range(0,4):
    recherche()     
    print(sum(liste_somme))

print("*****************")