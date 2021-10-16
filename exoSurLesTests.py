import unittest
import math
# Exo 1
'''
Ecrire le test unitaire d’une fonction qui retourne le cube de son argument
'''

def cube (a):
    cube = a*a*a
    return cube
print(cube(2))

# Exo 2
'''
Ecrire  la  fonction  qui  calcule  le  volume  d’une  sphère  et  écrire  le  test  unitaire 
correspondant
'''
def volumeSphere (r):
    v = 4/3*math.pi*r*r
    return v

# Exo 3
'''
Ecrire le test d’une fonction qui calcule le pgcd de deux nombres.
'''

def pgcd(a,b):
    if a == 0 or b == 0:
        return None
    if a < b:
        minimum = a
    else :
        minimum = b
    diviseurs = []
    for i in range ( 1, minimum + 1):
        if a % i == 0 and b % i == 0:
            diviseurs.append(i)
    return diviseurs[-1]


# Exo 4

'''
Ecrire le test d’une fonction qui prend trois arguments en paramètre et retourne le 
maximum de ces trois arguments.
'''
def pgn(a,b,c):
    pgn = max(a,b,c)
    return pgn
print(pgn(4,3,5))

# Exo 5
'''
Ecrire une fonction dont le prototype est : def 
table_multiplication(mul,borninf,bornsup) , qui affiche la table de multiplication  
par  mul,  d’une  borne  inférieure  à  une  borne  supérieure.  Ecrire  le  test  unitaire 
correspondant.
'''
def table_multiplication(mul,borninf,bornsup):
    while borninf <= bornsup:
        tableMul = borninf * mul
        print(tableMul)
        borninf = borninf + 1
    
table_multiplication(2,2,6)

# Exo 6
'''
Ecrire une fonction qui prend 2 listes en paramètres, et retourne le résultat des 2 
listes fusionnées. Ecrire le test unitaire correspondant.
'''
def fusion (a, b):
    fusion = a + b
    return fusion
print(fusion ([1,2,3],[4,5,6]))

# Exo 7
'''
Tester automatiquement la fonction qui prend une liste en paramètre et retourne 
son inverse.
'''
def inverseDeLaListe(a):
    #inverse = reversed(a)
    return a.reverse()
    #return inverse
print(inverseDeLaListe([1,2,3]))


class TestCube(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(0), (0))
        self.assertEqual(cube(2), (8))
        self.assertEqual(cube(-3), (-27))
'''
class TestVolumeSphere(unittest.TestCase):
    def test_volumeSphere(self):
        self.assertEqual(volumeSphere(0), (0))
        self.assertEqual(volumeSphere(2), (16.75))
        self.assertEqual(volumeSphere(-3), (37,69))
'''
class TestPgcd(unittest.TestCase):
    def test_pgcd(self):
        self.assertEqual(pgcd(12, 8), 4)
        self.assertIsNone(pgcd(0, 1),None)
        self.assertIsNone(pgcd(1, 0),None)

class TestPgn(unittest.TestCase):
    def test_pgn(self):
        self.assertEqual(pgn(0,1,3), (3))
        self.assertEqual(pgn(3,1,0), (3))
        self.assertEqual(pgn(1,3,0), (3))

class TestFusion(unittest.TestCase):
    def test_fusion(self):
        self.assertEqual(fusion([],[]), ([]))
        self.assertEqual(fusion([3],[0]), ([3,0]))
        self.assertEqual(fusion([1,3,0],[4,5,6]), ([1,3,0,4,5,6]))
        self.assertEqual(fusion([1,1,1,1,1],[1,1,1,1,1]), ([1,1,1,1,1,1,1,1,1,1]))
if __name__ == '__main__':
    unittest.main()

