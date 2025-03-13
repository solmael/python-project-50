def format_stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    result = ['{']
    
    for item in diff:
        key = item['key']
        item_type = item['type']
        
        if item_type == 'nested':
            child = format_stylish(item['children'], depth + 1)
            result.append(f"{indent}    {key}: {child}")
        elif item_type == 'unchanged':
            value = format_value(item['value'], depth + 1)
            result.append(f"{indent}    {key}: {value}")
        elif item_type == 'added':
            value = format_value(item['new_value'], depth + 1)
            result.append(f"{indent}  + {key}: {value}")
        elif item_type == 'removed':
            value = format_value(item['old_value'], depth + 1)
            result.append(f"{indent}  - {key}: {value}")
        elif item_type == 'changed':
            old_val = format_value(item['old_value'], depth + 1)
            new_val = format_value(item['new_value'], depth + 1)
            result.append(f"{indent}  - {key}: {old_val}")
            result.append(f"{indent}  + {key}: {new_val}")
    
    result.append(f"{indent}}}")
    return '\n'.join(result)


def format_value(value, depth):
    indent = ' ' * (depth * 4)
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            formatted = format_value(v, depth + 1)
            lines.append(f"{indent}    {k}: {formatted}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value == '':
        return ''
    return str(value)