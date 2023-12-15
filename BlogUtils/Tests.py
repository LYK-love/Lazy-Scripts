import unittest
from BlogUtils import collect_elements

class TestMyModuleFunctions(unittest.TestCase):

    def test_collect_elements(self):
        result = collect_elements([3,4])
        self.assertEqual(result, [3,4])

        result = collect_elements(3)
        self.assertEqual(result, [3])

        result = collect_elements([[3], [4]])
        self.assertEqual(result, [3, 4])




if __name__ == '__main__':
    unittest.main()
