# encoding: utf-8


def string_permutations(s1, s2):
    if len(s1) == len(s2):
        if sorted(s1) == sorted(s2):
            return True
        return False
    return False


def test():
    print string_permutations('cobra', 'baroc')
    print string_permutations('dog', 'dug')
    print string_permutations('boat', 'garden')
    print string_permutations('doctorwho', 'torchwood')


if __name__ == "__main__":
    test()
