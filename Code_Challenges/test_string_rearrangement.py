import unittest
from string_rearrangement2 import *

class TestStringRearrangement(unittest.TestCase):
    
    def test_single_letter(self):
        data = ['q','q']
        self.assertFalse(stringsRearrangement(data))
    
    def test_repeated_letters(self):
        data = ["zzzzab", "zzzzbb", "zzzzaa"]
        self.assertTrue(stringsRearrangement(data))
    
    def test_six(self):
        data = ["abc", "bef", "bcc", "bec", "bbc", "bdc"]
        self.assertTrue(stringsRearrangement(data))

if __name__ == '__main__':
    unittest.main()