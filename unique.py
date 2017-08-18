# encoding: utf-8
import unittest


def is_unique(s):
    uniques = set()
    for c in s:
        if c in uniques:
            return False
        uniques.add(c)
    return True


class Testint(unittest.TestCase):
    def test():
        print is_unique('test')
    print is_unique('cobra')
    print is_unique('thisreqpolxcvbnmdf')


if __name__ == "__main__":
    test()
