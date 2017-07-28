# encoding: utf-8
import unittest


def string_permutations(s1, s2):
    if len(s1) == len(s2):
        if sorted(s1) == sorted(s2):
            return True
        return False
    return False


class Testing(unittest.TestCase):
    def test(self):
        self.assertTrue(string_permutations('cobra', 'baroc'))
        self.assertFalse(string_permutations('dog', 'dug'))
        self.assertFalse(string_permutations('boat', 'garden'))
        self.assertTrue(string_permutations('doctorwho', 'torchwood'))


if __name__ == "__main__":
    unittest.main()
