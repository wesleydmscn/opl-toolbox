import os
import time

print('''\033[96m

 __ _     __    _  _  _  __
/  / \|\||_    |_||_)|_)(_ 
\__\_/| ||  ___| ||  |  __)
 __ __    __ _  _ ___ _  _ 
/__|_ |\||_ |_)|_| | / \|_)
\_||__| ||__| \| | | \_/| \ 

\033[00m''')

ROOT_DIR = 'APPS/'
CONF_FILE = 'conf_apps.cfg'


def init_script():
    if os.path.isdir(ROOT_DIR):
        find_elf_files()
    else:
        print('APPS/ folder not found.')


def find_elf_files():
    files = os.listdir(ROOT_DIR)
    elf_files = [f for f in files if f.endswith('.ELF')]

    if not elf_files:
        print('.elf files not found.')
        return

    print(60 * '-')
    print('The following .elf were found:')
    print(f'\033[96m{elf_files}\033[00m')
    print(60 * '-')

    create_conf_apps(elf_files)


def create_conf_apps(elf_list):
    time.sleep(1)
    user_inputs = []

    for elf in elf_list:
        user_input = str(input(f'Name for this elf file ({elf}): '))
        user_inputs.append([user_input, elf])

    try:
        with open(CONF_FILE, 'w') as cfg:
            for path in user_inputs:
                cfg.write(f'{path[0]}=mass:/{ROOT_DIR}{path[1]}\n')

            print(60 * '-')
            print(f'\033[92m\n{CONF_FILE} was created\033[00m\n')
            print(60 * '-')

    except Exception as e:
        print(f'An error occured while writing the file: {e}')


init_script()