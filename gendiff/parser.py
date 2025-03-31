import json

import yaml


def parse_file(file, format):
    if not file.strip():
        return {}
    
    match format:
        case 'json':
            return json.loads(file)
        case 'yml' | 'yaml':
            return yaml.safe_load(file)
        case _:
            raise ValueError(f"Unsupported format: {format}")
