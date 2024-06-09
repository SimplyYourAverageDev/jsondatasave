import json


def load(FileName: str):
    """
    This function is used to load data in the JSON Format.
    """
    with open(FileName, 'r') as file:
        Save_Data = json.load(file)
    return Save_Data


def save(Data, Filename: str):
    """
    This function is used to save data in the JSON Format.
    """
    with open(Filename, "w") as dump:
        json.dump(Data, dump)
    return Data
