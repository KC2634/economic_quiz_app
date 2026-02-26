import unittest # a testing framework
from quiz_data import load_questions # converts to dict
from quiz_utils import clean_name, presence_check, character_check, pattern_check, length_check

class TestSmoke(unittest.TestCase):

    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertNotEqual(6,1)

    def test_load_questions_runs(self):
        self.assertTrue(1)

class TestQuiz(unittest.TestCase):
    def test_load_questions_runs(self):
        questions = load_questions()
        self.assertIsNotNone(questions)

    def test_presence_check_happy(self):
        self.assertTrue(presence_check("Jo"))

    def test_clean_name(self):
        self.assertEqual(clean_name("  josh done  "), "Josh Done")
        self.assertEqual(clean_name("BON JONES"), "Bon Jones")
    
    def test_character_check_happy(self):
        self.assertTrue(character_check("Jo"))
        self.assertTrue(character_check("Joseph Smith"))

    def test_character_check_unhappy(self):
        self.assertFalse(character_check("Jess1"))
        self.assertFalse(character_check("897"))

    def test_symbol_check_happy(self):
        self.assertTrue(pattern_check("Anna-Marie"))
        self.assertTrue(pattern_check("Jo-C"))

if __name__ == "__main__":
    unittest.main()  

    
