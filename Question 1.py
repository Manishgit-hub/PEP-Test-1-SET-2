def get_dict_value(dct, path):
    keys = path.split(".")
    current = dct

    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None

    return current


dct = {
    "student": {
        "roll_number": "10",
        "class": "1st"
    },
    "teacher": {
        "school": "ABC"
    }
}

print(get_dict_value(dct, "student.roll_number"))
print(get_dict_value(dct, "teacher.roll_number"))
