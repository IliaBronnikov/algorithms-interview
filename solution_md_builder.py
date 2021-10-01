import sys
import argparse
import ast
comment = '<!--  -->'

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name_task_block')
    parser.add_argument('code', type=open)
    parser.add_argument('name_task',nargs='+')
    return parser

def read_data(text_file):
    data = ''
    with open(text_file) as s:
        data = s.read()
    s.close()
    return data

def build_constr_get_leetcode_sol(name_task, text_solution):
    NameTask = ' '.join(name_task)
    NameTask_L = '-'.join(name_task).lower()
    link = 'https://leetcode.com/problems/'
    key_text = '+ [{}](#{})\n'.format(NameTask, NameTask_L)
    value_text = '\n\n## {}\n\n{}{}\n\n```python\n{}\n```'.format(NameTask, link, NameTask_L, text_solution)
    return {key_text:value_text}


def get_splitted_md(old_md_file):
    return {old_md_file.split(comment)[0]:old_md_file.split(comment)[1]}

def get_full_md(old_md_file, new_md_file):
    return list(old_md_file.keys())[0] + list(new_md_file.keys())[0] + comment + list(old_md_file.values())[0] + \
           list(new_md_file.values())[0]

def write_data(name_file, full_text):
    with open(name_file, mode = 'w') as p:
        for line in full_text:
            p.write(line)
    p.close()

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    old_md = read_data(namespace.name_task_block.lower() + '.md')
    TASK_SOLUTION = read_data('text_solution.txt')

    prep_sol = build_constr_get_leetcode_sol(namespace.name_task, TASK_SOLUTION)
    old_md_split = get_splitted_md(old_md)
    new_md = get_full_md(old_md_split, prep_sol)

    write_data(namespace.name_task_block.lower() +'.md', new_md)





