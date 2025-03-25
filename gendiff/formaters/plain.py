def format_plain(diff, path=''):
    result = []
    for node in diff:
        match node:
            case {'key': key, 'type': 'nested', 'children': children}:
                nested_path = f'{path}.{key}' if path else key
                result.append(format_plain(children, nested_path))
            case {'key': key, 'type': 'added', 'new_value': new_val}:
                current_path = f'{path}.{key}' if path else key
                result.append(f"Property '{current_path}' "
                              f"was added with value: {check_value(new_val)}")
            case {'key': key, 'type': 'removed'}:
                current_path = f'{path}.{key}' if path else key
                result.append(f"Property '{current_path}' was removed")
            case {'key': key, 'type': 'changed', 
                  'old_value': old, 'new_value': new}:
                current_path = f'{path}.{key}' if path else key
                result.append(f"Property '{current_path}' was updated. "
                              f"From {check_value(old)} to {check_value(new)}")
            case _:
                continue
    return '\n'.join(result)


def check_value(value):
    match value:
        case dict():
            return '[complex value]'
        case None:
            return 'null'
        case bool() | int():
            return str(value).lower()
        case str():
            return f"'{value}'"
        case _:
            return str(value)
        

def get_format_plain(diff):
    return format_plain(diff)