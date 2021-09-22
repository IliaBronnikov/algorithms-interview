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

def read_data(task_block):
    with open(task_block.lower() +'.md', mode = 'r') as s:
        s.readline()
        s.readline()
        full = s.readlines()

    with open('text_solution.txt') as f:
        TASK_SOLUTION = f.readlines()

    s.close()
    f.close()

    return full, TASK_SOLUTION

def update_md_file(list_full_text, TASK_SOLUTION):
        TASK_LINK = 'https://leetcode.com/problems/' + '-'.join(namespace.name_task).lower() + '/'
        TASK_TITLE = ' '.join(namespace.name_task)
        link_suffix = TASK_LINK.split("/")[-2]
        list_full_text.insert(list_full_text.index('\n'), '+ [{}](#{})\n'.format(TASK_TITLE, link_suffix))
        list_full_text.append('\n\n## {}\n\n{}\n\n```python\n{}\n```\n'\
        .format(TASK_TITLE, TASK_LINK, build_code_block(TASK_SOLUTION)))

def record_new_md_file(task_block, list_full_text):
    with open(task_block.lower() +'.md', mode = 'w') as p:
        p.write('#' + task_block.title() +'\n\n')
        for line in list_full_text:
            p.write(line)
    p.close()


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    full_text, TASK_SOLUTION = read_data(namespace.name_task_block)
    update_md_file(full_text, TASK_SOLUTION)
    record_new_md_file(namespace.name_task_block, full_text)





