import os

def init_script():
  root_dir = os.listdir()

  if 'APPS' in root_dir:
    find_elf_files()
  else:
    print('404, APPS folder not found.')

def find_elf_files():
  files = os.listdir('APPS/')
  match_list = []

  for elf_file in files:
    if '.ELF' in elf_file:
      match_list.append(elf_file)

  if len(match_list) == 0:
    print('.elf files not found.')
  else:
    print(match_list)
    create_conf_apps(match_list)

def create_conf_apps(elf_list):
  user_inputs = []

  for elf in elf_list:
    user_input = str(input(f'Which name should appear in the APPS list for this elf: {elf}? '))
    user_inputs.append([user_input, elf])
  
  cfg = open('conf_apps.cfg', 'w')

  for path in user_inputs:
    cfg.write(f'{path[0]}=mass:/APPS/{path[1]}\n')
    
  cfg.close()

init_script()