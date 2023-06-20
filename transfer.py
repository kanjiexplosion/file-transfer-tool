import os
import sys
import shutil
from argparse import ArgumentParser

def main(src, dist, dry):
    if os.path.isdir(src) and os.path.isdir(dist):
        src_files = os.listdir(src)
        dist_files = os.listdir(dist)

        copy_file_list = []
        ng_prefix_list = ['.', 'NC_FLLST.DAT']
        for file in src_files:
            if file in dist_files:
                continue
            else:
                for prefix in ng_prefix_list:
                    if file.startswith(prefix):
                        break
                else:
                    copy_file_list.append(file)
                    continue

        print('\n--- copy file list ---\n')
        for i, file in enumerate(copy_file_list):
            print(f'{i+1}, {file}')
        print('\n')

        if not dry:
            for file in copy_file_list:
                src_fpath = os.path.join(src, file)
                dist_fpath = os.path.join(dist, file)
                shutil.copyfile(src_fpath, dist_fpath)
            print('\n--- done ---\n')
        sys.exit(0)
    else:
        print('\n--- error! ----')
        print('source or destination does not exist.')
        print('check the args, try again.\n')
        sys.exit(1)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('source', help='file transfer source')
    parser.add_argument('destination', help='file transfer destination')
    parser.add_argument('--dry', action='store_true', help='dry run')

    args = parser.parse_args()

    main(args.source, args.destination, args.dry)
