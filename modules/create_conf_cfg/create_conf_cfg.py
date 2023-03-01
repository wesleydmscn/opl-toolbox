import sys

sys.path.insert(0, '../file_management')

from popstarter import find_popstarter
from popstarter import create_popstarter_instance

CONF_FILE = 'conf_apps.cfg'

def create_conf_cfg(file_type, file_list_by_type, directory):
    user_inputs = []

    for file in file_list_by_type:
        user_input = str(input(f'Name for this {file_type} file ({file}), or (jump): '))

        if user_input == 'jump':
            continue
        else:
            user_inputs.append([user_input, file])

    try:
        if file_type == 'VCD':
            if find_popstarter(directory):
                popstarter_path = find_popstarter(directory)
                create_popstarter_instance(popstarter_path, user_inputs)

                with open(CONF_FILE, 'a') as cfg:
                    for path in user_inputs:
                        cfg.write(f'{path[0]}=mass:/{directory}XX.{path[1].replace(".VCD", ".ELF")}\n')

                print(60 * '-')
                print(f'\033[92m\n{CONF_FILE} was created\033[00m\n')
                print(60 * '-')
            else:
                return

        else:
            with open(CONF_FILE, 'a') as cfg:
                for path in user_inputs:
                    cfg.write(f'{path[0]}=mass:/{directory}{path[1]}\n')

            print(60 * '-')
            print(f'\033[92m\n{CONF_FILE} was created\033[00m\n')
            print(60 * '-')

    except IOError as e:
        print(f'An error occurred while writing to the file: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
