import os

options = f'''\033[96m
 __ _     __    _  _  _  __
/  / \|\||_    |_||_)|_)(_ 
\__\_/| ||  ___| ||  |  __)
 __ __    __ _  _ ___ _  _ 
/__|_ |\||_ |_)|_| | / \|_)
\_||__| ||__| \| | | \_/| \ 

{60 * '-'}

  1 - Automatic listing for OPL APPS/ folder only.
  2 - Automatic listing for OPL POPS/ folder only.

{60 * '-'}
\033[00m'''

def conf_options():
    print(options)

    while True:
        try:
            user_choice = int(input("What do you want to do?: "))

            if user_choice in [1, 2]:
                if user_choice == 1:
                    return ['ELF', 'APPS/']
                else:
                    return ['VCD', 'POPS/']
            else:
                print(60 * '-')
                print('Option not found. Try again with 1 or 2!')
                print(60 * '-')
        except ValueError:
            print(60 * '-')
            print('Invalid input. Try again with 1 or 2!')
            print(60 * '-')
