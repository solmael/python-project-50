from .json import get_format_json
from .plain import get_format_plain
from .stylish import get_format_stylish


def format_diff(diff, format_name='stylish'):
    formatters = {
        'stylish': get_format_stylish,
        'plain': get_format_plain,
        'json': get_format_json
    }
    
    formatter = formatters.get(format_name)
    return formatter(diff)