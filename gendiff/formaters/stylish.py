INDENT_SIZE = 4


def format_stylish(diff, depth=0):
    indent = ' ' * (depth)
    lines = []
    
    for node in diff:
        key = node['key']
        
        if node['type'] == 'nested':
            value = format_stylish(node['children'], depth + INDENT_SIZE)
            lines.append(f'{indent}    {key}: {value}')
            
        elif node['type'] == 'unchanged':
            value = format_value(node['value'], depth + INDENT_SIZE)
            lines.append(f'{indent}    {key}: {value}')
            
        elif node['type'] == 'added':
            value = format_value(node['new_value'], depth + INDENT_SIZE)
            lines.append(f'{indent}  + {key}: {value}')
            
        elif node['type'] == 'removed':
            value = format_value(node['old_value'], depth + INDENT_SIZE)
            if value == "":
                lines.append(f'{indent}  - {key}:')
            else:
                lines.append(f'{indent}  - {key}: {value}')
            
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'], depth + INDENT_SIZE)
            new_value = format_value(node['new_value'], depth + INDENT_SIZE)
            if old_value == "":
                lines.append(f'{indent}  - {key}:')
            else:
                lines.append(f'{indent}  - {key}: {old_value}')
            if new_value == "":
                lines.append(f'{indent}  + {key}:')
            else:
                lines.append(f'{indent}  + {key}: {new_value}')
    
    result = '{\n' + '\n'.join(lines) + f'\n{" " * depth}}}'
    return result


def format_value(value, depth):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = ' ' * (depth)
        lines = []
        for k, v in sorted(value.items()):
            formatted_v = format_value(v, depth + INDENT_SIZE)
            lines.append(f'{indent}    {k}: {formatted_v}')
        result = '{\n' + '\n'.join(lines) + f'\n{indent}}}'
        return result
    else:
        return str(value)