import solution_md_builder as smb
import unittest


class TestBuilder(unittest.TestCase):
    IN_STR = 'Test name\nhttps://leetcode.com/\nclass\n    1stline\n    2ndline'
    OUT_STR = '+ [Test name](#test-name)\n<!--  -->2\n\n## Test name\n\nhttps://leetcode.com/test-name/\n\n' \
              '```python\n1stline\n2ndline\n```'


    def test_build_constr_get_leetcode_sol(self):
        out_dict = {'md_link':'+ [Test name](#test-name)\n',
            'code_block': '\n\n## Test name\n\nhttps://leetcode.com/test-name/\n\n```python\n1stline\n2ndline\n```'}
        self.assertCountEqual(smb.build_constr_get_leetcode_sol(IN_STR), out_dict)


    def test_get_splitted_md(self):
        input_str = '+ [Va Pal](#va-pal)\n<!--  -->\n## Va Pal'
        out_dict = {'md_link':'+ [Va Pal](#va-pal)\n', 'code_block': '## Va Pal'}
        self.assertCountEqual(smb.get_splitted_md(input_str, 'string.md'), out_dict)


    def test_get_full_md(self):
        self.assertCountEqual(smb.get_full_md({'md_link':'1', 'code_block':'2'},{'md_link':'3', 'code_block':'4'}),
        '13<!--  -->24')


    def test_content_new_md_file_notempty_md(self):
        out_str = '+ [Test name](#test-name)\n<!--  -->2\n\n## Test name\n\nhttps://leetcode.com/test-name/\n\n' \
                  '```python\n1stline\n2ndline\n```'
        self.assertCountEqual(smb.get_content_new_md_file(IN_STR, '1<!--  -->2', 'string.md'), '1{}'.format(out_str))


    def test_content_new_md_file_empty_md(self):
        out_str = '+ [Test name](#test-name)\n<!--  -->\n\n## Test name\n\nhttps://leetcode.com/test-name/\n\n' \
                  '```python\n1stline\n2ndline\n```'
        self.assertCountEqual(smb.get_content_new_md_file(IN_STR, '', 'string.md'), '# String\n\n{}'.format(out_str))

if __name__ == "__main__":
    unittest.main()