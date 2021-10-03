import sys
import argparse
import re
MD_FILE_DELIMITER = '<!--  -->'


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


def get_link_from_text(text_data):
    return re.search(r'https://.*problems/', text_data).group(0)


def build_constr_get_leetcode_sol(name_task, text_solution, link):
    name_task_str = ' '.join(name_task)
    name_task_low_str = '-'.join(name_task).lower()
    key_text = '+ [{}](#{})\n'.format(name_task_str, name_task_low_str)
    value_text = '\n\n## {}\n\n{}{}/\n\n```python\n{}\n```'.format(name_task_str, link, name_task_low_str,
                                                                   text_solution)
    return {'md_link':key_text, 'code_block':value_text}


def get_splitted_md(old_md_file):
    return {'md_link': old_md_file.split(MD_FILE_DELIMITER)[0],'code_block' :old_md_file.split(
                                                                  MD_FILE_DELIMITER)[1]}


def get_full_md(old_md_file, new_md_file):
    return '{}{}{}{}{}'.format(old_md_file['md_link'], new_md_file['md_link'], MD_FILE_DELIMITER, old_md_file[
        'code_block'], new_md_file['code_block'])


def write_data(name_file, full_text):
    with open(name_file, mode = 'w') as p:
        p.write(full_text)
    p.close()

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    old_md = read_data(namespace.name_task_block.lower() + '.md')
    task_solution = read_data('text_solution.txt')
    link = get_link_from_text(old_md)

    prepared_solution = build_constr_get_leetcode_sol(namespace.name_task, task_solution, link)
    old_md_split = get_splitted_md(old_md)
    new_md = get_full_md(old_md_split, prepared_solution)

    write_data(namespace.name_task_block.lower() +'.md', new_md)





