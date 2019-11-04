"""
This function is capable of reading json. When it reads it returns an array of object
"""
import json


def json_read(file_path):
    try:
        with open(file_path) as f_in:
            return json.load(f_in)
    except Exception as e:
        print("Json reading issue")
        return e