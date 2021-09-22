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

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    TASK_LINK = 'https://leetcode.com/problems/' + '-'.join(namespace.name_task).lower() + '/'
    TASK_TITLE = ' '.join(namespace.name_task)

    with open('text_solution.txt') as f:
        TASK_SOLUTION = f.readlines()
    f.close()

    with open(namespace.name_task_block.lower() +'.md', mode = 'r+') as s:
        s.readline()
        s.readline()
        full = s.readlines()
        link_suffix = TASK_LINK.split("/")[-2]
        full.insert(full.index('\n'), '+ [{}](#{})\n'.format(TASK_TITLE, link_suffix))
        full.append('\n\n## {}\n\n{}\n\n```python\n{}\n```\n'\
        .format(TASK_TITLE, TASK_LINK, build_code_block(TASK_SOLUTION)))
    s.close()

    with open(namespace.name_task_block.lower() +'.md', mode = 'w') as p:
        p.write('#' + namespace.name_task_block.title() +'\n\n')
        for line in full:
            p.write(line)
    p.close()




