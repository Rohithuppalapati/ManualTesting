import unittest
import source_code

class Test_Source_code(unittest.TestCase):

    def test_method(self):
        test_parameter=5
        result=source_code.code(test_parameter)
        self.assertEqual(result,15)

    def test_method2(self):
        test_parameter=''
        result=source_code.code(test_parameter)
        self.assertTrue(result)

    def test_method3(self):
        test_parameter=None
        result=source_code.code(test_parameter)
        self.assertEqual(result,'please give number')

    def test_method4(self):
        test_parameter='None'
        result=source_code.code(test_parameter)
        self.assertIsInstance(result,ValueError)

if __name__ == '__main__':
    unittest.main()

