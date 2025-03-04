INDENT_SIZE = 4


def format_stylish(diff, depth=0):
    indent = ' ' * (INDENT_SIZE * depth)
    lines = []
    
    for node in diff:
        key = node['key']
        
        if node['type'] == 'nested':
            value = format_stylish(node['children'], depth + 1)
            lines.append(f'{indent}    {key}: {value}')
            
        elif node['type'] == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{indent}    {key}: {value}')
            
        elif node['type'] == 'added':
            value = format_value(node['new_value'], depth + 1)
            lines.append(f'{indent}  + {key}: {value}')
            
        elif node['type'] == 'removed':
            value = format_value(node['old_value'], depth + 1)
            if value == '':
                lines.append(f'{indent}  - {key}:')
            else:
                lines.append(f'{indent}  - {key}: {value}')
            
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            if old_value == '':
                lines.append(f'{indent}  - {key}:')
            else:
                lines.append(f'{indent}  - {key}: {old_value}')
            if new_value == '':
                lines.append(f'{indent}  + {key}:')
            else:
                lines.append(f'{indent}  + {key}: {new_value}')
    
    result = '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    return result


def format_value(value, depth):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = ' ' * (INDENT_SIZE * depth)
        lines = []
        for k, v in sorted(value.items()):
            formatted_v = format_value(v, depth + 1)
            lines.append(f'{indent}    {k}: {formatted_v}')
        result = '{\n' + '\n'.join(lines) + f'\n{indent}}}'
        return result
    else:
        return str(value)
