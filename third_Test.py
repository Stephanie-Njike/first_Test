import unittest 
def mediane(a,b,c):
    if a <= b and b <= c:
       return b
    if a <= c and c <= b:
       return c
    if b <= a and a <= c:
       return a
    if b <= c and c <= a:
       return c
    if c <= b and b <= a:
       return b
    if c <= a and a <= b:
       return a

class TestMediane(unittest.TestCase):
    def test_mediane1(self):
        self.assertEqual(mediane(2,2,2), 2)
        self.assertEqual(mediane(1,2,3), 2)
        self.assertEqual(mediane(1,6,4), 4)  
        self.assertEqual(mediane(8,-3,11), 8)
        self.assertEqual(mediane(6,2,5), 5)  
        self.assertEqual(mediane(5,8,3), 5)
        self.assertEqual(mediane(14,12,10), 12)
if __name__ == '__main__':
    unittest.main()
         



       
