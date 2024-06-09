# jsondatasave

## Overview

jsondatasave is a Python library that provides a set of functions to facilitate working with JSON data. It includes functionalities to load, save, append, update, and delete data in JSON files, as well as support for custom encoders and decoders. The aim is to simplify common tasks associated with JSON data management while handling potential errors gracefully.

## Installation

To use this library, simply include it in your Python project. No additional installation steps are required.

## Functions

### `load(FileName: str) -> Any`

Loads data from a JSON file.

- **Parameters:**
  - `FileName`: The name of the file to load.
  
- **Returns:**
  - The data loaded from the JSON file.
  
- **Exceptions:**
  - Prints an error message if the file does not exist or contains invalid JSON.

### `save(Data: Any, Filename: str, pretty: bool = False, encoder: Optional[json.JSONEncoder] = None) -> Any`

Saves data to a JSON file.

- **Parameters:**
  - `Data`: The data to save.
  - `Filename`: The name of the file to save the data to.
  - `pretty`: If `True`, the JSON is pretty-printed with an indentation of 4 spaces. Default is `False`.
  - `encoder`: Optional custom JSON encoder.
  
- **Returns:**
  - The saved data.
  
- **Exceptions:**
  - Prints an error message if an unexpected error occurs during the save operation.

### `append(Data: Any, Filename: str, encoder: Optional[json.JSONEncoder] = None) -> Any`

Appends data to an existing JSON file containing a JSON array.

- **Parameters:**
  - `Data`: The data to append.
  - `Filename`: The name of the file to append the data to.
  - `encoder`: Optional custom JSON encoder.
  
- **Returns:**
  - The updated data.
  
- **Exceptions:**
  - Prints an error message if the file does not contain a JSON array or if an unexpected error occurs.

### `load_with_decoder(FileName: str, decoder: Optional[json.JSONDecoder] = None) -> Any`

Loads data from a JSON file using a custom decoder.

- **Parameters:**
  - `FileName`: The name of the file to load.
  - `decoder`: Optional custom JSON decoder.
  
- **Returns:**
  - The data loaded from the JSON file.
  
- **Exceptions:**
  - Prints an error message if the file does not exist or contains invalid JSON.

### `update(Filename: str, key: str, value: Any, encoder: Optional[json.JSONEncoder] = None) -> Any`

Updates a specific key in a JSON file.

- **Parameters:**
  - `Filename`: The name of the file to update.
  - `key`: The key to update.
  - `value`: The new value for the key.
  - `encoder`: Optional custom JSON encoder.
  
- **Returns:**
  - The updated data.
  
- **Exceptions:**
  - Prints an error message if the file does not contain a JSON object or if an unexpected error occurs.

### `delete(Filename: str, key: str, encoder: Optional[json.JSONEncoder] = None) -> Any`

Deletes a specific key from a JSON file.

- **Parameters:**
  - `Filename`: The name of the file to update.
  - `key`: The key to delete.
  - `encoder`: Optional custom JSON encoder.
  
- **Returns:**
  - The updated data.
  
- **Exceptions:**
  - Prints an error message if the file does not contain a JSON object, the key does not exist, or if an unexpected error occurs.

## Error Handling

The library handles common errors such as file not found, invalid JSON format, and unexpected exceptions. Error messages are printed to the console to inform the user of the issue.

## Examples

### Loading a JSON File

```python
data = load('data.json')
```

### Saving Data to a JSON File

```python
save(data, 'data.json', pretty=True)
```

### Appending Data to a JSON File

```python
append(new_data, 'data.json')
```

### Loading a JSON File with a Custom Decoder

```python
data = load_with_decoder('data.json', decoder=CustomDecoder)
```

### Updating a Key in a JSON File

```python
update('data.json', 'key_to_update', new_value)
```

### Deleting a Key from a JSON File

```python
delete('data.json', 'key_to_delete')
```

## License

This library is provided as-is, without warranty of any kind. Use at your own risk.