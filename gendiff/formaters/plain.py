def format_plain(diff, path=''):
    result = []

    for node in diff:
        key = node['key']
        current_path = f'{path}.{key}' if path else key

        if node['type'] == 'nested':
            result.append(format_plain(node['children'], current_path))
        elif node['type'] == 'added':
            value = format_value_for_plain(node['new_value'])
            result.append(
                f"Property '{current_path}' "
                f'was added with value: {value}')
        elif node['type'] == 'removed':
            result.append(f"Property '{current_path}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value_for_plain(node['old_value'])
            new_value = format_value_for_plain(node['new_value'])
            result.append(
                f"Property '{current_path}' was updated. "
                f'From {old_value} to {new_value}')
        elif node['type'] == 'unchanged':
            continue

    return '\n'.join(result)


def format_value_for_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)