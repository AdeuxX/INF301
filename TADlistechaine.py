from execution_time import mesure_time

class ListeChainee:
    liste_vide = () 
    def __init__(self,elem,next=liste_vide):
        assert next is ListeChainee.liste_vide or isinstance(ListeChainee)
        self.elem = elem
        self.next = next
@mesure_time
def insert(l,elem):
    return ListeChainee(elem,l)
@mesure_time
def recherche(l,element_recherche):
    element_liste = l.elem
    next_elem = l.next
    i=0
    while next_elem != ():
        if element_liste == element_recherche :
            return i
        i +=1
        element_liste = next_elem.elem
        next_elem = element_liste.next
        #changer "element contient pas de next remplacer ca par les listes"
    return Exception("element introuvable ")
@mesure_time
def suppr_elem(l,element_a_suppr):
    try :
        index = recherche(l,element_a_suppr)
        ieme_maillon = l 
        for i in range(0,index):
            element_itérer = ieme_maillon.element
            ieme_maillon = ieme_maillon.next
            #refaire en recurssif pour pouvoir remonter ( remplir la fin avant le début)

    except:
        Exception("element introuvable")