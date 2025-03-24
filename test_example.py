import unittest
import main
from unittest.mock import patch

class TestStringMethods(unittest.TestCase):
    
    def test_Dud(self):

        self.assertEqual(main.Dud(), "A!")

    def test_inputControl(self, mock_input):
        
        self.assertEqual(main.inputControl(), 1)

    def test_characterChoiceConfirmation(self, mock_input):

        self.assertTrue(main.characterChoiceConfirmation())

    def test_harderInputControl(self):

        self.assertIsNotNone(main.harder_input_control())

if __name__ == '__main__':

    unittest.main()
