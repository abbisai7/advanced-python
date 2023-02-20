#unittest 

import unittest

import calc 

class TestCalc(unittest.TestCase):  #testsuite
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__ == "__main__":
    unittest.main()    
        
    