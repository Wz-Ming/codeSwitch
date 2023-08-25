#!/usr/bin/python3
from pathlib import Path
import chardet
import sys
arg=None
if len(sys.argv)>1:
    arg=sys.argv[1]

def detect_encoding(pathFile:Path):
    with open(pathFile, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encode = result['encoding']
        confidence = result['confidence']
        return encode, confidence

def searchFile(path:Path):
    suffixList=['.h','.c','.cpp','.hpp','.py']
    if path.exists():
        for file in path.iterdir():
            if file.is_dir():
                searchFile(file)
            elif file.is_file():
                if file.suffix in suffixList:
                    if file.name != 'encodeswitch.py':
                        encode,confidence = detect_encoding(file)
                        print(f" {file} {encode} {confidence}")
                        if arg=='gbk':
                            if encode=='utf-8' or encode=='ascii':
                                file.write_bytes(file.read_text(encoding=encode).encode('gb2312'))
                        else:
                            if encode != 'utf-8' and encode !='ascii' and file.name != 'encodeswitch.py':
                                file.write_bytes(file.read_text(encoding=encode).encode('utf-8'))
searchFile(Path().absolute())
