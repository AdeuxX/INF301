from execution_time import mesure_time
class ArbreBinaire :
    def __init__(self, item, next_left=None, next_right=None):
        self.item = item
        self.right = next_right
        self.left = next_left
@mesure_time
def insert(arbre, element):
    if arbre == None:
        return element
    if element < arbre.key:
        return ArbreBinaire(arbre.item, insert(arbre.next_left,element), arbre.next_right)
    elif element > arbre.key:
        return ArbreBinaire(arbre.item, arbre.next_left ,insert(arbre.next_right,element))
    else:
        return Exception("element égaux")
@mesure_time
def recherche(arbre, element_recherche):
    if arbre.key == element_recherche:
        return arbre.item
    if element_recherche < arbre.key : 
        recherche(arbre.next_left,element_recherche)
    elif element_recherche> arbre.key:
        recherche(arbre.next_right,element_recherche)
@mesure_time
def suppr():
    ...
    