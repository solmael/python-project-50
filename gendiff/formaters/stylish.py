def get_indent(depth):
    return ' ' * (depth * 4)


def format_block(lines, depth):
    indented_lines = [f'{get_indent(depth)}{line}' for line in lines]
    indented_lines.append(f'{get_indent(depth)}}}')
    return '\n'.join(indented_lines)


def add_braces(content):
    return f'{{\n{content}'


def format_item(item, depth):
    key = item['key']
    item_type = item['type']
    match item_type:
        case 'nested':
            children = format_stylish(item['children'], depth + 1)
            return [f'    {key}: {children}']
        case 'unchanged':
            value = format_value(item['value'], depth + 1)
            return [f'    {key}: {value}']
        case 'added':
            value = format_value(item['new_value'], depth + 1)
            return [f'  + {key}: {value}']
        case 'removed':
            value = format_value(item['old_value'], depth + 1)
            return [f'  - {key}: {value}']
        case 'changed':
            old_val = format_value(item['old_value'], depth + 1)
            new_val = format_value(item['new_value'], depth + 1)
            return [
                f'  - {key}: {old_val}',
                f'  + {key}: {new_val}'
            ]
        case _:
            raise ValueError(f'Unknown type: {item_type}')


def format_stylish(diff, depth=0):
    lines = []
    for item in diff:
        lines.extend(format_item(item, depth))
    block = format_block(lines, depth)
    return add_braces(block)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            formatted_v = format_value(v, depth + 1)
            lines.append(f'    {k}: {formatted_v}')
        block = format_block(lines, depth)
        return add_braces(block)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value == '':
        return ''
    return str(value)


def get_format_stylish(diff):
    return format_stylish(diff)