INDENT_SIZE = 4


def format_line(base_indent, prefix, key, value_str):
    if value_str == '':
        return f"{base_indent}{prefix}{key}:"
    else:
        return f"{base_indent}{prefix}{key}: {value_str}"


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


def format_value(value, depth):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        current_indent = ' ' * (INDENT_SIZE * depth)
        lines = []
        for k, v in sorted(value.items()):
            key_indent = current_indent + ' ' * INDENT_SIZE
            formatted_v = format_value(v, depth + 1)
            lines.append(format_line(key_indent, '', k, formatted_v))
        return '{\n' + '\n'.join(lines) + f'\n{current_indent}}}'
    elif isinstance(value, str):
        return value
    else:
        return str(value)