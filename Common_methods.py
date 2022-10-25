from random import randint

def enter (message):
    num = int(input(message))
    return num

def create_string (different_chars):
    symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    text = ''
    for i in range (different_chars):
        amount_symb = randint(1, 5)
        text += amount_symb * symbols[randint(0, 51)]
    return text

def compression (encode_txt, decode_txt):
    result = round((1 - len(encode_txt) / len(decode_txt)) * 100, 2)
    return result