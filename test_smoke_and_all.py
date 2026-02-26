import unittest # a testing framework
from quiz_data import load_questions # converts to dict
from quiz_utils import clean_name, presence_check, character_check, pattern_check, length_check #cleans the name, checks the presence, validates the name, checks the patterns are valid and checks the length of the name

class TestSmoke(unittest.TestCase):

    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertNotEqual(6,1)

    def test_load_questions_runs(self):
        self.assertTrue(1)

class TestQuiz(unittest.TestCase):
    def test_load_questions_runs(self):
        questions = load_questions()
        self.assertIsNotNone(questions) # tests the questions run

    def test_presence_check_happy(self):
        self.assertTrue(presence_check("Jo")) # tests the name is not empty

    def test_clean_name(self):
        self.assertEqual(clean_name("  josh done  "), "Josh Done") # tests the name is cleansed
        self.assertEqual(clean_name("BON JONES"), "Bon Jones")
    
    def test_character_check_happy(self):
        self.assertTrue(character_check("Jo")) # tests the name only contains only valid characters (no numbers)
        self.assertTrue(character_check("Joseph Smith"))

    def test_character_check_unhappy(self):
        self.assertFalse(character_check("Jess1")) # false test for numbers in name
        self.assertFalse(character_check("897"))

    def test_symbol_check_happy(self):
        self.assertTrue(pattern_check("Anna-Marie")) # tests the name only contains valid punctuation
        self.assertTrue(pattern_check("Jo-C"))

    def test_symbol_check_unhappy(self):
        self.assertFalse(pattern_check("Anna]k")) # false test for invalid punctuation
        self.assertFalse(pattern_check("Jo/C"))

    def test_length_check_happy(self):
        self.assertTrue(length_check("Jo")) # tests for valid length of the name
        self.assertTrue(length_check("Hanahhhhhhhhhhhhhhhhhhhhhhhhhhhh"))

    def test_length_check_unhappy(self):
        self.assertFalse(length_check("J")) # false test for incorrect length of name
        self.assertFalse(length_check("Hanahhhhhhhhhhhhhhhhhhhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

if __name__ == "__main__":
    unittest.main()  

    
