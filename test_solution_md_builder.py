from solution_md_builder import *
import unittest

class TestBuilder(unittest.TestCase):
    def test_build_constr_get_leetcode_sol_1(self):
        self.assertCountEqual(build_constr_get_leetcode_sol(['Valid', 'Palindrome'], 'I am the best'),
                               {'new_md_link':'+ [Valid Palindrome](#valid-palindrome)\n', 'new_code_block': '\n\n## '
                                                                                                             'Valid '
                                                                             'Palindrome\n'
                                                                             '\nhttps://leetcode.com/problems/'
                                                                             'valid-palindrome\n\n```python\nI am '
                                                                             'the best\n```'})

    def test_get_splitted_md_1(self):
        self.assertCountEqual(get_splitted_md('+ [Va Pal](#va-pal)\n<!--  -->\n## Va Pal'),{'old_md_link':'+ [Va Pal]('
                                                                                            '#va-pal)\n',
                                                                                            'old_code_block': '## Va '
                                                                                                              'Pal'})
    def test_get_splitted_md_2(self):
        self.assertCountEqual(get_splitted_md('abc<!--  -->cba'),{'old_md_link' : 'abc','old_code_block':'cba'})

    def test_get_full_md_1(self):
        self.assertCountEqual(get_full_md({'old_md_link':'1', 'old_code_block':'2'},{'new_md_link':'3',
                                                                                     'new_code_block':'4'}),
        '13<!--  -->24')

if __name__ == "__main__":
    unittest.main()