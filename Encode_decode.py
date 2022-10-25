def rle_encode(data_input):
    encoding = ''
    count = 1
    if not data_input:
        return ''
    for ind in range(1, len(data_input)):
        if data_input[ind] == data_input[ind - 1]:
            count += 1
        else :
            if count == 1:
                encoding += data_input[ind - 1]
            else:
                encoding += str(count) + data_input[ind - 1]
                count = 1
    else:
        if count == 1:
            encoding += data_input[ind]
        else:
            encoding += str(count) + data_input[ind]
    return encoding

def rle_decode(data_output):
    decoding = ''
    count = ''
    for char in data_output:
        if char.isdigit():
            count += char
        else :
            if not count:
                decoding += char
            else: 
                decoding += int(count) * char
                count = ''
    return decoding