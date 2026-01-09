# pyospackage-tirthjoshi

A practice Python package created for DSCI 524 Individual Assignment 1.

## Description

This package provides simple mathematical functions for adding and subtracting numbers. It demonstrates the basic structure of a Python package following pyOpenSci guidelines.

## Installation

### From TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ pyospackage-tirthjoshi
```

### From source

```bash
git clone https://github.com/tirthjoshi/pyospackage-tirthjoshi.git
cd pyospackage-tirthjoshi
pip install -e .
```

## Usage

```python
from pyospackage_tirthjoshi.example import add_num, subtract_num

# Add two numbers
result = add_num(5, 3)
print(result)  # Output: 8

# Subtract two numbers
result = subtract_num(10, 4)
print(result)  # Output: 6
```

## Features

- `add_num(a, b)`: Add two numbers
- `subtract_num(a, b)`: Subtract two numbers

## Development

This package was created as a learning exercise following the [pyOpenSci Python Package Guide](https://www.pyopensci.org/python-package-guide/).

## License

MIT License
