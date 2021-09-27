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


'''Ecrire une fonction qui permet de calculer le plus grand diviseur d'un nombre a,qui est le plus grand nombre (sauf a lui-même) tel que la division de a par ce naturel est une division entière.
Étant donné que 0 est divisible par n'importe quel naturel, cela peut causer des problèmes si vous recherchez le plus grand, nous nous attendons donc à ce que vous renvoyiez Aucun.
1 renvoie également Aucun.
Rappelons que l'opérateur % renvoie le reste de la division euclidienne.'''

def plusGrandDiviseur(a):
    if a == 0 or a == 1:
        return None
    diviseurs = []
    for i in range ( 1, a):
        if a % i == 0:
            diviseurs.append(i)
    return diviseurs[-1]
print(plusGrandDiviseur(990))

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
            total = sum(tab)
            self.assertEqual(somme(tab), total,
                             "Votre fonction appliquée à "+str(tab)+
                             " a retourné "+str(somme(tab))+" et non "+
                             str(total))

class TestPlusGrandDiviseur(unittest.TestCase):
    def test_plusGrandDiviseur(self):
        self.assertEqual(plusGrandDiviseur(686), 343)
        self.assertEqual(plusGrandDiviseur(12), 6, "Votre fonction appliquée à "+str(12)+
                             " a retourné "+str(plusGrandDiviseur(12))+" et non "+
                             str(6)) 
        self.assertEqual(plusGrandDiviseur(990), 495)
        self.assertEqual(plusGrandDiviseur(4), 2)
        self.assertIsNone(plusGrandDiviseur(0),None)
        self.assertIsNone(plusGrandDiviseur(1),None)

        
    
    
        


if __name__ == '__main__':
    unittest.main()



