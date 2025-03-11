INDENT_SIZE = 4


def format_stylish(diff, depth=0):
    indent = ' ' * depth
    lines = []
    
    for node in diff:
        key = node.get('key', '')
        
        if node.get('type') == 'nested':
            value = format_stylish(node['children'], depth + INDENT_SIZE)
            lines.append(f"{indent}    {key}: {value}")
            
        elif node.get('type') == 'unchanged':
            value_str = format_value(node['value'], depth + INDENT_SIZE)
            lines.append(f"{indent}    {key}: {value_str}")
            
        elif node.get('type') == 'added':
            value_str = format_value(node['new_value'], depth + INDENT_SIZE)
            if value_str == '':
                lines.append(f"{indent}  + {key}:")
            else:
                lines.append(f"{indent}  + {key}: {value_str}")
                
        elif node.get('type') == 'removed':
            value_str = format_value(node['old_value'], depth + INDENT_SIZE)
            if value_str == '':
                lines.append(f"{indent}  - {key}:")
            else:
                lines.append(f"{indent}  - {key}: {value_str}")
                
        elif node.get('type') == 'changed':
            old_val = format_value(node['old_value'], depth + INDENT_SIZE)
            new_val = format_value(node['new_value'], depth + INDENT_SIZE)
            
            if old_val == '':
                lines.append(f"{indent}  - {key}:")
            else:
                lines.append(f"{indent}  - {key}: {old_val}")
                
            if new_val == '':
                lines.append(f"{indent}  + {key}:")
            else:
                lines.append(f"{indent}  + {key}: {new_val}")
                
    if not lines:
        return '}'
    
    return '{\n' + '\n'.join(lines) + f'\n{indent}}}'


def format_value(value, depth):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = ' ' * depth
        lines = []
        for key, val in value.items():
            formatted_value = format_value(val, depth + INDENT_SIZE)
            lines.append(f"{indent}    {key}: {formatted_value}")
        return '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    elif isinstance(value, str):
        return value if value else ''
    else:
        return str(value)
