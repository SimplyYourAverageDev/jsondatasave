
---

`jsondatasave` Documentation

## Introduction

`jsondatasave` is a simple Python library that facilitates the process of storing and retrieving JSON data. It provides an intuitive interface to read and write JSON data to and from files.

## Installation

To install `jsondatasave`, you can use `pip`:

```
pip install jsondatasave
```

## Features

- Simple JSON data reading and writing.
- Minimalistic API with just two main functions: `load` and `save`.

## Functions

### `load(FileName)`

This function reads a JSON file and returns its content as a Python dictionary.

**Parameters**:
- `FileName` (`str`): The path to the JSON file that you wish to read.

**Returns**:
- `dict`: The content of the JSON file as a Python dictionary.

**Example**:

```python
data = load("sample.json")
print(data)
```

### `save(Data, Filename)`

This function writes a Python dictionary to a JSON file.

**Parameters**:
- `Data` (`dict`): The Python dictionary that you wish to save to a file.
- `Filename` (`str`): The path to the file where the data should be saved.

**Returns**:
- `dict`: The same Python dictionary that was provided as input.

**Example**:

```python
data = {"name": "John", "age": 30}
save(data, "output.json")
```

## Dependencies

Currently, there are no external dependencies for this library. The comment in `setup.py` regarding 'hashl' is not related to the provided functions.

## License

`jsondatasave` is licensed under the MIT license.

## Author

Created by YourAverageDev.

---