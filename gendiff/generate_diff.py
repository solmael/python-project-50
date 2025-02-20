from gendiff.reader import read_files


def generate_diff(file1_path, file2_path):
    file1_data, file2_data = read_files(file1_path, file2_path)
    
    all_keys = sorted(set(file1_data.keys()) | set(file2_data.keys()))
    
    diff = []
    for key in all_keys:
        if key not in file1_data:
            diff.append(f"  + {key}: {file2_data[key]}")
        elif key not in file2_data:
            diff.append(f"  - {key}: {file1_data[key]}")
        elif file1_data[key] == file2_data[key]:
            diff.append(f"    {key}: {file1_data[key]}")
        else:
            diff.append(f"  - {key}: {file1_data[key]}")
            diff.append(f"  + {key}: {file2_data[key]}")
    
    return "{\n" + "\n".join(diff) + "\n}"
