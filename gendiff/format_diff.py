from gendiff.formaters import format_stylish
from gendiff.formaters import format_plain

def format_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")