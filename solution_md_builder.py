import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name_task_block')
    parser.add_argument('code', type=open)
    parser.add_argument('name_task',nargs='+')
    return parser

def build_code_block(solution):
    return ''.join([line for line in solution])

def read_data(text_file):
    with open(text_file) as s:
        list_name = s.readlines()
    s.close()
    return list_name

def build_constr_get_leetcode_sol(name_task, text_solution):
    NT = ' '.join(name_task)
    NT_L = '-'.join(name_task).lower()
    return {'+ [{}](#{})\n'.format(NT, NT_L):'\n\n## ' + NT + '\n\nhttps://leetcode.com/problems/' + NT_L +
                                            '\n\n```python\n' + text_solution + '\n```'}

def get_splitted_md(old_md_file):
    return {old_md_file.split('<!--  -->')[0]:old_md_file.split('<!--  -->')[1]}

def get_full_md(old_md_file, new_md_file):
    return list(old_md_file.keys())[0] + list(new_md_file.keys())[0] + '<!--  -->' + list(old_md_file.values())[0] + \
           list(new_md_file.values())[0]

def record_data(name_file, full_text):
    with open(name_file, mode = 'w') as p:
        for line in full_text:
            p.write(line)
    p.close()

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    old_md = read_data(namespace.name_task_block.lower() + '.md')
    old_md = build_code_block(old_md)
    TASK_SOLUTION_LIST = read_data('text_solution.txt')
    TASK_SOLUTION_STR = build_code_block(TASK_SOLUTION_LIST)

    prep_sol = build_constr_get_leetcode_sol(namespace.name_task, TASK_SOLUTION_STR)
    old_md_split = get_splitted_md(old_md)
    new_md = get_full_md(old_md_split, prep_sol)

    record_data(namespace.name_task_block.lower() +'.md', new_md)





