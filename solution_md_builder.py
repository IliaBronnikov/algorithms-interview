import sys
import argparse
import re
MD_FILE_DELIMITER = '<!--  -->'


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('code')
    parser.add_argument('name_task_block')
    return parser


def read_data(text_file):
    data = ''
    with open(text_file) as s:
        data = s.read()
    return data


def build_constr_get_leetcode_sol(text_solution):
    name_task = re.match(r'.*\b', text_solution).group(0)
    name_link = re.search(r'https://.*/', text_solution).group(0)
    key_text = '+ [{}](#{})\n'.format(name_task, '-'.join(name_task.lower().split()))
    value_text = '\n\n## {}\n\n{}{}/\n\n```python\n{}\n```'.format(name_task, name_link,  '-'.join(name_task.lower(
    ).split()), '\n'.join([line[4:] for line in text_solution.split('\n')[3:]]))
    return {'md_link':key_text, 'code_block':value_text}


def get_splitted_md(old_md_file, name_task_block):
    if old_md_file:
        splitted_md_file = old_md_file.split(MD_FILE_DELIMITER)
        return {'md_link': splitted_md_file[0],'code_block' :splitted_md_file[1]}
    else:
        return {'md_link': '# {}\n\n'.format(name_task_block.split('.')[0].capitalize()),'code_block' :''}

def get_full_md(old_md_file, new_md_file):
    return '{}{}{}{}{}'.format(old_md_file['md_link'], new_md_file['md_link'], MD_FILE_DELIMITER, old_md_file[
        'code_block'], new_md_file['code_block'])


def write_data(name_file, full_text):
    with open(name_file, mode = 'w') as p:
        p.write(full_text)
    p.close()


def content_new_md_file(task_solution, old_md, name_task_block):
    prepared_solution = build_constr_get_leetcode_sol(task_solution)
    old_md_split = get_splitted_md(old_md, name_task_block)
    return get_full_md(old_md_split, prepared_solution)


def main():
    parser = createParser()
    arg = parser.parse_args(sys.argv[1:])
    name_task_block = arg.name_task_block
    code = arg.code

    old_md = read_data(name_task_block)
    task_solution = read_data(code)

    write_data(name_task_block, contain_new_md_file(task_solution, old_md, name_task_block))


if __name__ == '__main__':
    main()






