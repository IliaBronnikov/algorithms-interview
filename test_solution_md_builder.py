from solution_md_builder import *
import unittest

class TestBuilder(unittest.TestCase):
    def test_build_constr_get_leetcode_sol_1(self):
        self.assertCountEqual(build_constr_get_leetcode_sol(['Valid', 'Palindrome'], 'I am the best'),
                               {'+ [Valid Palindrome](#valid-palindrome)\n': '\n\n## Valid '
                                                                             'Palindrome\n'
                                                                             '\nhttps://leetcode.com/problems/'
                                                                             'valid-palindrome\n\n```python\nI am '
                                                                             'the best\n```'})

    def test_get_splitted_md_1(self):
        self.assertCountEqual(get_splitted_md('+ [Va Pal](#va-pal)\n<!--  -->\n## Va Pal'),{'+ [Va Pal]('
                                                                                            '#va-pal)\n': '## Va Pal'})
    def test_get_splitted_md_2(self):
        self.assertCountEqual(get_splitted_md('abc<!--  -->cba'),{'abc':'cba'})

    def test_get_full_md_1(self):
        self.assertCountEqual(get_full_md({'1':'2'},{'3':'4'}), '13<!--  -->24')

if __name__ == "__main__":
    unittest.main()