from Common_methods import create_string as create
from Common_methods import enter
from Common_methods import compression

from Import_export import import_to_file as to_file
from Import_export import export_from_file as from_file

from Encode_decode import rle_encode as encode
from Encode_decode import rle_decode as decode

import os

os.system('cls')

different_chars = enter('Введите количество различных символов в изначальной строке: ')
original_text = create (different_chars)
print(f'Информация в исходном в виде: {original_text}')

file = 'Data_input.txt'
to_file (original_text, file)
print(f'Исходная информация записана в файл \'Data_input.txt\'')

data_input = from_file (file)


encode = encode(data_input)
print(f'Информация в сжатом виде: {encode}')

file = 'Data_encoding.txt'
to_file(encode, file)
print('Сжатая информация записана в файл \'Data_encoding.txt\'')

encode = from_file(file)

decode = decode(encode)
file = 'Data_output.txt'
to_file(decode, file)
print(f'Декодированная информация в виде: [{decode}] записана в файл \'Data_output.txt\'')


print(f'Степень сжатия информации составила {compression (encode, decode)}%')