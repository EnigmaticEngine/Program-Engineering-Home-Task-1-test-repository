
# wNumber = int(input("Please, state the number of the current worldline: "))
# print("Hello, Worldline #", wNumber)

import unittest
import main

class TestStringMethods(unittest.TestCase):
    
    def test_Dud(self):

        self.assertEqual(main.Dud(), "A!")

    def test_inputControl(self):
        
        self.assertEqual(main.inputControl(), 1)

    def test_characterChoiceConfirmation(self):

        self.assertTrue(main.characterChoiceConfirmation())

    def test_harderInputControl(self):

        self.assertIsNotNone(main.harderInputContol())

if __name__ == '__main__':

    unittest.main()
