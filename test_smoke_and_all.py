import unittest # a testing framework
from quiz_data import load_questions # converts to dict
from quiz_utils import clean_name, presence_check, character_check, pattern_check, length_check

class TestSmoke(unittest.TestCase):

    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertNotEqual(6,1)

if __name__ == "__main__":
    unittest.main()  

    
