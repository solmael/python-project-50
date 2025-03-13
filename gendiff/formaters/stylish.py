INDENT_SIZE = 4


def format_line(indent, prefix, key, value_str):
    if value_str.startswith('{'):
        return f"{indent}{prefix}{key}: {value_str}"
    elif '\n' in value_str:
        return f"{indent}{prefix}{key}:{value_str}"
    elif not value_str:
        return f"{indent}{prefix}{key}:"
    return f"{indent}{prefix}{key}: {value_str}"


def format_value(value, depth):
    if value is None:
        return 'null'
    elif value == 'none':
        return 'none'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value == '':
        return ''
    elif value == 0:
        return '0'
    elif isinstance(value, dict):
        return format_dict(value, depth)
    else:
        return str(value)


def format_dict(dict_value, depth):
    indent = ' ' * (INDENT_SIZE * depth)
    lines = []
    for key, value in dict_value.items():
        value_str = format_value(value, depth + 1)
        lines.append(format_line(indent, '    ', key, value_str))
    
    if not lines:
        return '{}'
    
    close_indent = ' ' * (INDENT_SIZE * depth)
    return '{\n' + '\n'.join(lines) + f'\n{close_indent}}}'


def format_stylish(diff, depth=0):
    indent = ' ' * (INDENT_SIZE * depth)
    lines = []
    
    for node in diff:
        key = node.get('key', '')
        status = node.get('type', '')
        
        if status == 'nested':
            value = format_stylish(node['children'], depth + 1)
            lines.append(format_line(indent, '    ', key, value))
        elif status == 'unchanged':
            value_str = format_value(node['value'], depth + 1)
            lines.append(format_line(indent, '    ', key, value_str))
        elif status == 'added':
            value_str = format_value(node['new_value'], depth + 1)
            lines.append(format_line(indent, '  + ', key, value_str))
        elif status == 'removed':
            value_str = format_value(node['old_value'], depth + 1)
            lines.append(format_line(indent, '  - ', key, value_str))
        elif status == 'changed':
            old_val = format_value(node['old_value'], depth + 1)
            new_val = format_value(node['new_value'], depth + 1)
            lines.append(format_line(indent, '  - ', key, old_val))
            lines.append(format_line(indent, '  + ', key, new_val))
    
    if not lines:
        return '{}'
    
    result = '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    return result.strip() if depth == 0 else result