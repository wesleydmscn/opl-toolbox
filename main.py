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
    
    files = find_files_by_type(conf_options_selected[0], conf_options_selected[1])

    if files == FileNotFoundError:
        return
    
    create_conf_cfg(files[0], files[1], conf_options_selected[1])

init_script()