
import unittest
import calc

def my_abs(a):
    if a <= 0:
        return -a
    return a

def my_abs1(b):
    if b <= 0:
        return b
    return b

"""Fct which calculates the sum of two numbers"""

def somme (a,b):
    return a+b

"""Fct which calculates the substraction of two numbers"""

def substraction (c,d):
    return c-d


"""Fct which calculates the multiplication of two numbers"""

def multiplication (e,f):
    return e*f

"""Fct which calculates the division of two numbers"""

def division (g,h):
	if h == 0:
		break
	else:
    return g/h

"""fct which takes a name as a parameter and which returns 'Hello' + name"""

def hello(nom):
    return 'Hello' + nom

"""Fct which say if a number is odd or even"""

def pair (nombre):
    return nombre % 2 == 0

def impair (nombre):
    return nombre % 2 != 0

class TestAbs(unittest.TestCase):
    
    def test_my_abs(self):
    	"""
        Check that my_app function is working correctly 
        """
        self.assertEqual(my_abs(5), 5)
        self.assertEqual(my_abs(0), 0)
        self.assertEqual(my_abs(-5), 5)

        self.assertEqual(my_abs1(5), 5)
        self.assertEqual(my_abs1(0), 0)
        self.assertEqual(my_abs1(-5), 5)
        # This assertion will launch an error
        #self.assertEqual(my_abs2(-5), 5)

class testCalc(unittest.TestCase):
	def test_somme(self):
		result = calc.somme(2,5)

        self.assertEqual(hello('Stephanie'), Stephanie)
        self.assertEqual(result, 7)
        self.assertEqual(calc.somme(-2,5), 3)
        self.assertEqual(calc.somme(-2,-5), -7)

    def test_substraction(self):

        self.assertEqual(calc.substraction(2,7), -5)
        self.assertEqual(calc.substraction(-2,7), -9)
        self.assertEqual(calc.substraction(-2,-7), 5)

    def test_multiplication(self):

        self.assertEqual(calc.multiplication(2,5), 10)
        self.assertEqual(calc.smultiplication(-2,5), -10)
        self.assertEqual(calc.multiplication(-2,-5), 10)

    def test_division(self):

        self.assertEqual(calc.division(2,2), 1)
        self.assertEqual(calc.division(-2,2), -1)
        self.assertEqual(calc.division(-2,-2), 1)
        

if __name__ == '__main__':
    unittest.main()
