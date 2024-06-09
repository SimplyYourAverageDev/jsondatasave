import json
from typing import Any, Optional

def load(FileName: str) -> Any:
    """
    This function is used to load data in the JSON Format.
    """
    try:
        with open(FileName, 'r') as file:
            Save_Data = json.load(file)
        return Save_Data
    except FileNotFoundError:
        print(f"Error: The file {FileName} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {FileName} contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def save(Data: Any, Filename: str, pretty: bool = False, encoder: Optional[json.JSONEncoder] = None) -> Any:
    """
    This function is used to save data in the JSON Format.
    """
    try:
        with open(Filename, "w") as dump:
            if pretty:
                json.dump(Data, dump, indent=4, cls=encoder)
            else:
                json.dump(Data, dump, cls=encoder)
        return Data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append(Data: Any, Filename: str, encoder: Optional[json.JSONEncoder] = None) -> Any:
    """
    This function is used to append data to an existing JSON file.
    """
    try:
        existing_data = load(Filename)
        if not isinstance(existing_data, list):
            print(f"Error: The file {Filename} does not contain a JSON array.")
            return
        existing_data.append(Data)
        save(existing_data, Filename, encoder=encoder)
        return existing_data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_with_decoder(FileName: str, decoder: Optional[json.JSONDecoder] = None) -> Any:
    """
    This function is used to load data in the JSON Format with a custom decoder.
    """
    try:
        with open(FileName, 'r') as file:
            Save_Data = json.load(file, cls=decoder)
        return Save_Data
    except FileNotFoundError:
        print(f"Error: The file {FileName} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {FileName} contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def update(Filename: str, key: str, value: Any, encoder: Optional[json.JSONEncoder] = None) -> Any:
    """
    This function is used to update a specific key in the JSON file.
    """
    try:
        data = load(Filename)
        if isinstance(data, dict):
            data[key] = value
            save(data, Filename, encoder=encoder)
            return data
        else:
            print(f"Error: The file {Filename} does not contain a JSON object.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete(Filename: str, key: str, encoder: Optional[json.JSONEncoder] = None) -> Any:
    """
    This function is used to delete a specific key from the JSON file.
    """
    try:
        data = load(Filename)
        if isinstance(data, dict):
            if key in data:
                del data[key]
                save(data, Filename, encoder=encoder)
                return data
            else:
                print(f"Error: The key {key} does not exist in the file {Filename}.")
        else:
            print(f"Error: The file {Filename} does not contain a JSON object.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")