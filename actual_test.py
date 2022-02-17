import unittest
import actual

class actual_test(unittest.TestCase):

    def test1(self):
        is_magician=False
        is_expert=True
        result=actual.magic(is_magician,is_expert)
        self.assertTrue(result)

    def test2(self):
        is_magician=False
        is_expert=False
        result=actual.magic(is_magician,is_expert)
        self.assertEqual(result,'you need magic')

    def test3(self):
        is_magician=int('sstr')
        is_expert=False
        result=actual.magic(is_magician,is_expert)
        self.assertIsInstance(result,ValueError)



if __name__ == '__main__':
    unittest.main()
