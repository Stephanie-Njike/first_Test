import unittest
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
    v = 4/3*pi*r*r
    return v

# Exo 3
'''
Ecrire le test d’une fonction qui calcule le pgcd de deux nombres.
'''

def pgcd(a):
    if a == 0 or a == 1:
        return None
    diviseurs = []
    for i in range ( 1, a):
        if a % i == 0:
            diviseurs.append(i)
    return diviseurs[-1]
print(pgcd(101))

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
if __name__ == '__main__':
    unittest.main()

