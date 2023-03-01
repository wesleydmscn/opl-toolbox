import os
import shutil

POPSTARTER_FILENAME = 'POPSTARTER.ELF'

def find_popstarter(directory):
    popstarter_path = os.path.join(directory, POPSTARTER_FILENAME)
    if os.path.isfile(popstarter_path):
        return popstarter_path
    else:
        print(60 * '-')
        print(f'Error: {POPSTARTER_FILENAME} not found in {directory}.')
        print(60 * '-')
        return None


def create_popstarter_instance(popstarter_path, files_to_instance):
    for file in files_to_instance:
        elf_filename = f'XX.{file[1].replace(".VCD", "")}.ELF'
        destination_path = os.path.join('POPS/', elf_filename)
        shutil.copyfile(popstarter_path, destination_path)

    print(60 * '-')
    print(f'\033\n[92mReference created successfully!\033[00m\n')
    print(60 * '-')
