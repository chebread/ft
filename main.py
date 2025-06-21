import argparse
import os
import sys
from colorama import init as colorama_init # pip install colorama

from lib.is_text_file import is_text_file
from lib.print_path import print_path

colorama_init()
parser = argparse.ArgumentParser(prog='ft', description='ft is a program to find for text in files.')
parser.usage = "ft [OPTIONS] [text] [path]..."

parser.add_argument('search_string', nargs='?', type=str, default='', help="string to search") # 코드 작성한 순서대로 '위치 인수'의 위치가 됨
parser.add_argument('search_path', nargs='?', type=str, default='.', help='path to search')
parser.add_argument('-V', '--version', action='version', version='%(prog)s 9.0')


args = parser.parse_args()
search_string_arg, search_path_arg = str(args.search_string), str(args.search_path) # tuple unpacking

current_path = os.getcwd()
search_path = current_path if search_path_arg == '.' else\
    (search_path_arg if os.path.exists(f"{search_path_arg}") else current_path)
# 찾는 디렉토리/파일이 존재하지 않으면 현재 디렉토리 기준으로 검색
# search_path는 파일/디렉토리임
is_file = os.path.isfile(search_path)
if is_file:
    # 파일일 때
    if is_text_file(search_path):
        try:
            with open(search_path, 'rt') as fin: # text_file이 binary일 수도 있으므로 예외 처리함
                is_found = False
                for text_line in fin:
                    if search_string_arg in text_line:
                        print_path(current_path, search_path)
                        is_found = True
                        break
                if is_found:
                    is_found = False
        except:
            pass
    else:
        # 텍스트 파일이 아님
        sys.exit(0)
else:
    # 디렉토리일 때
    dir_list = os.walk(search_path) # 현위치 및 모든 하위 나열
    text_files = [file for i in dir_list for j in i[2] if is_text_file(file := f"{i[0]}/{j}")] # 일반 텍스트 파일만 담기

    if search_string_arg == '': # 만약 빈 값을 찾으려고 한다면 => fd/ls와 똑같은 역할을 수행함
        for path in text_files:
            print_path(current_path, path)
    else:
        # 일반 텍스트에서 문자열 검색
        # 파일 사이즈도 구해서 text_files를 작은 파일 순서대로 정렬하기, -> 작은 파일부터 순차적으로 문자열 비교 처리
        # found_files = []
        is_found = False
        for text_file in text_files:
            try:
                with open(text_file, 'rt') as fin: # text_file이 binary일 수도 있으므로 예외 처리함
                # fin: 읽기용 파일
                # fout: 쓰기용 파일
                    for text_line in fin:
                        if search_string_arg in text_line:
                            # found_files.append(text_file)
                            print_path(current_path, text_file)
                            is_found = True
                            break
                    if is_found:
                        is_found = False
                        continue
            except:
                # 예외 발생
                pass