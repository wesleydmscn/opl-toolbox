import os

def find_files_by_type(file_type, directory):
    if not os.path.isdir(directory):
        print(f'Error: {directory} folder not found.')
        return FileNotFoundError

    all_files = os.listdir(directory)
    files_by_type = [f for f in all_files if f.endswith(f'.{file_type}')]

    if not files_by_type:
        print(f'Error: .{file_type} files not found in {directory}.')
        return FileNotFoundError

    print(60 * '-')
    print(f'The following {file_type} files were found in {directory}:')
    print(f'\033[96m{files_by_type}\033[00m')
    print(60 * '-')

    return [file_type, files_by_type]
