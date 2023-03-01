import sys

sys.path.insert(0, 'modules/prompts')
sys.path.insert(0, 'modules/file_management')
sys.path.insert(0, 'modules/create_conf_cfg')

from conf_options import conf_options
from find_files_by_type import find_files_by_type
from create_conf_cfg import create_conf_cfg

def init_script():
    conf_options_selected = conf_options()

    if not conf_options_selected:
        return

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