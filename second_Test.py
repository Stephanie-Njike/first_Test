
import unittest

# Solution 1
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



# Solution 2
def mediane1 (a,b,c):
    ##a,b,c=3,2,4
    if a>=b and a<=c:
        median=a
    elif b>=a and b<=c:
        median=c
    elif c>=a and c<=b:
        median=c
    return median
print(mediane1(6,4,5))
print(mediane1(2,2,2))
print(mediane1(1,2,3))
print(mediane1(8,-3,11))


# Solution 3
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
'''
class TestMediane(unittest.TestCase):
    def test_mediane(self):
        self.assertEqual(mediane(2,2,2), 2)
        self.assertEqual(mediane(1,2,3), 2)
        self.assertEqual(mediane(6,4,5), 5)
        self.assertEqual(mediane(8,-3,11), 8)


class TestMediane1(unittest.TestCase):
    def test_mediane1(self):
        self.assertEqual(mediane1(2,2,2), 2)
        self.assertEqual(mediane1(1,2,3), 2)
        self.assertEqual(mediane1(6,4,5), 5)
        self.assertEqual(mediane1(8,-3,11), 8)


class TestMediane(unittest.TestCase):
    def test_mediane2(self):
        self.assertEqual(mediane2(2,2,2), 2)
        self.assertEqual(mediane2(1,2,3), 2)
        self.assertEqual(mediane2(6,4,5), 5)
        self.assertEqual(mediane2(8,-3,11), 8)

if __name__ == '__main__':
    unittest.main()
'''


