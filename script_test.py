import unittest
import source_code

class TestMain(unittest.TestCase):

    def test1(self):
        test_parameter=10
        result=source_code.code(test_parameter)
        self.assertEqual(result,20)

    def test2(self):
        test_parameter='ssd'
        result=source_code.code(test_parameter)
        self.assertIsInstance(result,ValueError)

    def test3(self):
        test_parameter=''
        result=source_code.code(test_parameter)
        self.assertEqual(result,'please give number')

unittest.main()
