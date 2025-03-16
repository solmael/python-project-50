### Hexlet tests and linter status:
[![Actions Status](https://github.com/solmael/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/solmael/python-project-50/actions)

<a href="https://codeclimate.com/github/solmael/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/c45c3f5436e544dbd87e/maintainability" /></a>

<a href="https://codeclimate.com/github/solmael/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/c45c3f5436e544dbd87e/test_coverage" /></a>

[![gendiff](https://github.com/solmael/python-project-50/actions/workflows/gendiff.yml/badge.svg)](https://github.com/solmael/python-project-50/actions/workflows/gendiff.yml)

# ABOUT PROJECT 

Compares two files in JSON/YAML formats and outputs their differences in a structured form.

## Requirements 
- Python >= 3.10
- uv >= 0.5.24
- ruff >= 0.9.6
  
## INSTALLATION

To install, clone the repository:
```sh
git clone https://github.com/solmael/python-project-50.git
```
## Usage

To display usage information:

```sh
gendiff -h
```

Example of comparing two files:

```sh
gendiff file1.json file2.json
```

## Output Formats

### Stylish

The default format. Shows changes in a tree structure.

### Plain

A flat text format, convenient for human reading:

### JSON

Outputs the changes in JSON format, convenient for machine processing.

## Development

### Tests

To run tests, use:

```sh
make test
```

### Linter

To check the code with the linter, use:

```sh
make lint
```

**Comparison of two JSON files:**

![asciicast](https://asciinema.org/a/q2yg4uVZnFlpl4Qw2LE451p8q.gif)