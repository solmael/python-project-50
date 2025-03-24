from gendiff.formaters import format_json, format_plain, format_stylish


def format_diff(diff, format_name='stylish'):
    formatters = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json
    }
    
    formatter = formatters.get(format_name)
    if formatter:
        return formatter(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")