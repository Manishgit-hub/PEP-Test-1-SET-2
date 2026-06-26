def get_dict_value(dct, path):
    keys = path.split('.')
    current = dct
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current