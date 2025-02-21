from gendiff.reader import read_files


def generate_diff(file1_path, file2_path):
    file1_data, file2_data = read_files(file1_path, file2_path)
    
    all_keys = sorted(set(file1_data.keys()) | set(file2_data.keys()))
    
    diff = []
    for key in all_keys:
        value1 = format_value(file1_data.get(key))
        value2 = format_value(file2_data.get(key))
        
        if key not in file1_data:
            diff.append(f'  + {key}: {value2}')
        elif key not in file2_data:
            diff.append(f'  - {key}: {value1}')
        elif file1_data[key] == file2_data[key]:
            diff.append(f'    {key}: {value1}')
        else:
            diff.append(f'  - {key}: {value1}')
            diff.append(f'  + {key}: {value2}')
    
    return '{\n' + '\n'.join(diff) + '\n}'


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)