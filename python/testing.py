#!/usr/bin/env python

import unittest

class SimpleSortTestCase(unittest.TestCase):
    def setUp(self):
        self.list = [5, 10, 3, 6, 9, 4, 1, 8, 2, 7, 0]

    def test_sorted(self):
        test_list = sorted(self.list)
        self.assertEqual(test_list,
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         "wrong order after sort")

    def test_reverse_sorted(self):
        test_list = sorted(self.list, reverse=True)
        self.assertEqual(test_list,
                         [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                         "wrong order after sort")

    def test_length_sorted(self):
        test_list = sorted(self.list)
        self.assertEqual(len(test_list),
                         3,
                         "this test was supposed to fail")

def suite(klass):
    "Collect all test cases from klass into a suite."
    suite = unittest.TestLoader().loadTestsFromTestCase(klass)
    return suite

def main():
    runner = unittest.TextTestRunner()
    sort_suite = suite(SimpleSortTestCase)
    runner.run(sort_suite)

if __name__ == "__main__":
    main()
