TASK_LINK = 'https://leetcode.com/problems/valid-palindrome/'
TASK_TITLE = 'Valid Palindrome'
TASK_SOLUTION = '''    def isPalindrome(self, s: str) -> bool:
        r = re.sub('[^a-zA-Z0-9]', '', s)
        if len(r) == 1:
            return True
        r = r.lower()
        for i in range(len(r)//2):
            if r[i] != r[-i-1]:
                return False
        return True    '''
SOLUTION_MD_TEMPLATE = '+ [{}](#{})\n\n## {}\n\n{}\n\n```python\n{}\n```\n'


def build_code_block(solution):
    return '\n'.join([line[4:] for line in solution.split('\n')])


if __name__ == '__main__':
    link_suffix = TASK_LINK.split("/")[-2]
    result_md = SOLUTION_MD_TEMPLATE\
        .format(TASK_TITLE, link_suffix, TASK_TITLE, TASK_LINK, build_code_block(TASK_SOLUTION))
    print(result_md)

