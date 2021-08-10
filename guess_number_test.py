import guess_number
import unittest

class TestMain(unittest.TestCase):
    def test_guess_number(self):
        answer=5
        guess=5
        result=guess_number.run_guess(answer,guess)
        self.assertTrue(result)

    def test_guess_number_wrong_pred(self):
        answer=5
        guess=0
        result = guess_number.run_guess(answer,guess)
        self.assertFalse(result)

    def test_guess_number_wrong_number(self):
        answer=7
        guess=11
        result = guess_number.run_guess(answer,guess)
        self.assertFalse(result)

    def test_guess_number_string(self):
        answer=8
        guess=''
        result = guess_number.run_guess(answer,guess)
        self.assertFalse(result)


unittest.main()

