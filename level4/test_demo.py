import unittest
class MyTestcase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True) #add asertion here
    def test_add(self):
        self.assertEqual(30,20+10)

if __name__=='__main__':
    unittest.main()