def import_to_file(value, file):
    with open (file, 'w') as data:
        data.writelines(value)
    return

def export_from_file (file):
    with open (file, 'r') as data:
        data_input = data.read()
    return data_input