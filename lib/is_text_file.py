# import magic # pip install python-magic
# # additional need libmagic (brew install libmagic)

# def is_text_file(filepath):
#     try:
#         mime_type = magic.from_file(filepath, mime=True)
#         return mime_type.startswith('text/')
#     except magic.MagicException as error:
#         # 오류 발생
#         pass
#     except FileNotFoundError:
#         # 파일이 존재하지 않음
#         return False

import mimetypes

def is_text_file(filepath):
    mime_type, _ = mimetypes.guess_type(filepath) # 파일 이름만 보고 파일의 확장자를 추측함
    prefixes = ('text/')
    if mime_type:
        return mime_type.startswith(prefixes)
    return False
