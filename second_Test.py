
import unittest

# Solution 1
print('************** Premiere solution **************')
def mediane (a,b,c):
    if (a<= c and c<=b) or (b<=c and c<=a):
        median = c
    elif (b<=a and a<=c) or (c<=a and a<=b):
        median = a
    else:
        median = b
    return median
print(mediane(6,4,5))
print(mediane(2,2,2))
print(mediane(1,2,3))
print(mediane(8,-3,11))

print('************** Fin de la premiere solution **************')



# Solution 2
print('************** Deuxieme solution **************')
def mediane1 (a,b,c):
    ##a,b,c=3,2,4
    if a>=b and a<=c:
        median=a
    elif b>=a and b<=c:
        median=c
    elif c>=a and c<=b:
        median=c
    return median
#print(mediane1(6,4,5))
print(mediane1(2,2,2))
print(mediane1(1,2,3))
print(mediane1(8,-3,11))

print('************** Fin de la deuxieme solution **************')

# Solution 3
print('************** Troisieme solution **************')
def mediane2 (a,b,c):
    median = a
    if a < b < c and c < b < a :
        median = b
    if b < c < a and a < c < b :
        median = c
    return median
print(mediane2(6,4,5))
print(mediane2(2,2,2))
print(mediane2(1,2,3))
print(mediane2(8,-3,11))
print('************** Fin de la troisieme solution **************')

'''
print('************** Premiere solution **************')
class TestMediane(unittest.TestCase):    
    def test_mediane(self):
        self.assertEqual(mediane(2,2,2), 2)
        self.assertEqual(mediane(1,2,3), 2)
        self.assertEqual(mediane(6,4,5), 5)
        self.assertEqual(mediane(8,-3,11), 8)
print('************** Fin de la premiere solution **************')
'''
print('************** Deuxieme solution **************')
class TestMediane1(unittest.TestCase):
    def test_mediane1(self):
        self.assertEqual(mediane1(2,2,2), 2)
        self.assertEqual(mediane1(1,2,3), 2)
        self.assertEqual(mediane1(6,4,5), 5)
        self.assertEqual(mediane1(8,-3,11), 8)
print('************** Fin de la deuxieme solution **************')
'''
print('************** Troisieme solution **************')
class TestMediane2(unittest.TestCase):
    def test_mediane2(self):
        self.assertEqual(mediane2(2,2,2), 2)
        self.assertEqual(mediane2(1,2,3), 2)
        self.assertEqual(mediane2(6,4,5), 5)
        self.assertEqual(mediane2(8,-3,11), 8)


print('************** Fin de la troisieme solution **************')
'''
if __name__ == '__main__':
    unittest.main()



