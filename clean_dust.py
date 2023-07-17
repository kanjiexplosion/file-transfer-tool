import os
import sys
import shutil
import copy
from argparse import ArgumentParser

def main(root):
    if os.path.isdir(root):
        root_full = os.path.abspath(root)
        print(f'root: {root_full}\n')

        output_recursively_as_tree(root_full, 0)

        sys.exit(0)
    else:
        print('\n--- error! ----')
        print('source or destination does not exist.')
        print('check the args, try again.\n')
        sys.exit(1)

def output_recursively_as_tree(parent_path, depth, indent=None):
    parent_full_path = os.path.abspath(parent_path)

    if indent is None:
        indent = []
    idt_out = ''.join(indent)
    print(f'{idt_out}{os.path.basename(parent_full_path)}/')

    files = os.listdir(parent_full_path)
    children = []
    for file in files:
        file_full_path = os.path.join(parent_full_path, file)
        if os.path.isdir(file_full_path):
            children.append(file_full_path)
    children.sort()

    # 子供がいない場合はスキップ
    if len(children) == 0:
        return

    # 親から渡されたインデントの変換処理
    idt = ['│   ' if item == '├── ' else item for item in indent]
    idt = ['    ' if item == '└── ' else item for item in idt]

    # 最後の子供はインデントが異なるため個別処理
    for child in children[:-1]:
        new_idt = copy.deepcopy(idt)
        new_idt.append('├── ')
        output_recursively_as_tree(child, depth+1, indent=new_idt)
    new_idt = copy.deepcopy(idt)
    new_idt.append('└── ')
    output_recursively_as_tree(children[-1], depth+1, indent=new_idt)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('root', help='start dir')

    args = parser.parse_args()

    main(args.root)
