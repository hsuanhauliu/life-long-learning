import unittest
import LinkedList as ll

class TestSolution(unittest.TestCase):
    def test_ConvertToBase10(self):
        test1 = ll.LinkedList([1, 1, 1, 0, 0])
        self.assertEqual(28, ll.convertToBase10(test1))

        test2 = ll.LinkedList([0, 1, 0])
        self.assertEqual(2, ll.convertToBase10(test2))

        test3 = ll.LinkedList([0])
        self.assertEqual(0, ll.convertToBase10(test3))

        test4 = ll.LinkedList([1])
        self.assertEqual(1, ll.convertToBase10(test4))


if __name__ == '__main__':
    unittest.main()
