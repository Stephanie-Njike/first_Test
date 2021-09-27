''' Ecrire une fonction qui prend un tableau en parametre et calculer la somme des elements de ce tableau.
Puis ecrire le test correspondant.'''

import unittest
import random

def somme (tab):
    summe = 0
    for i in range(0, len(tab)):
        summe = summe + tab[i]
        #print( 'la somme de tab est : ',summe)
    return summe
print(somme([1,2,3]))



class TestSomme(unittest.TestCase):
    """
     Classe de test permettant de valider le bon fonctionnement de somme
    """

    def test_somme(self):
        """
        @pre: -
        @post: a verifie le fonctionnement correct de la fonction somme
        """
        # Liste contenant un seul élément
        tab = [random.randint(1, 9)]
        self.assertEqual(somme(tab), tab[0],
                         "Votre fonction appliquée à "+str(tab)+
                         " a retourné "+str(somme(tab))+" et non "+
                         str(tab[0]))
        # Liste triée contenant trois éléments
        for _ in range(10):
            summe = random.randint(3, 19)
            tab = [summe-random.randint(1, 5), summe,
                   summe+random.randint(3, 9)]
            total = sum(tab)
            self.assertEqual(somme(tab), total,
                             "Votre fonction appliquée à "+str(tab)+
                             " a retourné "+str(somme(tab))+" et non "+
                             str(total))

        # Liste triée contenant cinq éléments
        for _ in range(10):
            tab = [None] * 5
            tab[0] = random.randint(3, 19)
            for j in range(1, 5):
                tab[j] = tab[j-1]+random.randint(3, 19)
            median = tab[2]
            total = sum(tab)
            self.assertEqual(somme(tab), total,
                             "Votre fonction appliquée à "+str(tab)+
                             " a retourné "+str(somme(tab))+" et non "+
                             str(total))
        


if __name__ == '__main__':
    unittest.main()

