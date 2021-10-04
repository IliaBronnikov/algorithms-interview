import solution_md_builder as smb
import unittest

class TestBuilder(unittest.TestCase):
    def test_build_constr_get_leetcode_sol(self):
        self.assertCountEqual(smb.build_constr_get_leetcode_sol('Test name\nhttps://leetcode.com/\nclass\n    '
        '1stline\n    2ndline'), {'md_link':'+ [Test name](#test-name)\n', 'code_block': '\n\n## Test name\n'
        '\nhttps://leetcode.com/test-name/\n\n```python\n1stline\n2ndline\n```'})


    def test_get_splitted_md(self):
        self.assertCountEqual(smb.get_splitted_md('+ [Va Pal](#va-pal)\n<!--  -->\n## Va Pal', 'string.md'),
                              {'md_link':'+ [Va Pal]('
                                                                                            '#va-pal)\n',
                                                                                            'code_block': '## Va '
                                                                                                              'Pal'})


    def test_get_full_md(self):
        self.assertCountEqual(smb.get_full_md({'md_link':'1', 'code_block':'2'},{'md_link':'3',
                                                                                     'code_block':'4'}),
        '13<!--  -->24')


    def test_contain_new_md_file_notempty_md(self):
        self.assertCountEqual(smb.contain_new_md_file('Test name\nhttps://leetcode.com/\nclass\n    '
        '1stline\n    2ndline', '1<!--  -->2', 'string.md'), '1+ [Test name](#test-name)\n<!--  -->2\n\n## '
        'Test name\n\nhttps://leetcode.com/test-name/\n\n```python\n1stline\n2ndline\n```')


    def test_contain_new_md_file_empty_md(self):
        self.assertCountEqual(smb.contain_new_md_file('Test name\nhttps://leetcode.com/\nclass\n    '
        '1stline\n    2ndline', '', 'string.md'), '# String\n\n+ [Test name](#test-name)\n<!--  -->\n\n## Test '
                                                  'name\n\nhttps://'
                                     'leetcode.com/test-name/\n\n```python\n1stline\n2ndline\n```')

if __name__ == "__main__":
    unittest.main()