# 경로를 예쁘게 출력
from colorama import Fore, Style

def print_path(current_path, path_to_print):
    short_path = path_to_print.replace(current_path + '/', '', 1)
    if short_path.rfind('/') != -1:
        dir_path = short_path[0:short_path.rfind('/') + 1]
        file_path = short_path[short_path.rfind('/') + 1:]
        print(f"{Style.BRIGHT}{Fore.CYAN}{dir_path}{Style.RESET_ALL}{file_path}")
    else:
        print(short_path)