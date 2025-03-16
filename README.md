### Hexlet tests and linter status:
[![Actions Status](https://github.com/solmael/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/solmael/python-project-50/actions)

<a href="https://codeclimate.com/github/solmael/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/c45c3f5436e544dbd87e/maintainability" /></a>

<a href="https://codeclimate.com/github/solmael/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/c45c3f5436e544dbd87e/test_coverage" /></a>

[![gendiff](https://github.com/solmael/python-project-50/actions/workflows/gendiff.yml/badge.svg)](https://github.com/solmael/python-project-50/actions/workflows/gendiff.yml)

# About Project

Compares two files in JSON/YAML formats and outputs their differences in a structured form.

## Features
- Supports JSON and YAML formats
- Multiple output formats: stylish tree, plain text, JSON
- Recursive processing of nested structures
- Color highlighting for changes (+ added, - removed)

## Requirements 
- Python >= 3.10
- uv >= 0.5.24
- ruff >= 0.9.6
- pytest-cov >= 6.0.0
- pyyaml >= 6.0.2
  
## Installation

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

[![asciicast](https://asciinema.org/a/4DRZHeuA3QfctUbgfAfvLl4Hk.svg)](https://asciinema.org/a/4DRZHeuA3QfctUbgfAfvLl4Hk)

**Comparison of two YAML/YML files:**

[![asciicast](https://asciinema.org/a/A2bsefLxZkCZ3L1I6wRheBapv.svg)](https://asciinema.org/a/A2bsefLxZkCZ3L1I6wRheBapv)

**Comparison of two files with a recursive structure: YAML/YML or JSON:**

[![asciicast](https://asciinema.org/a/TfxaRtAeE4ff0GqZuV2Z19cu7.svg)](https://asciinema.org/a/TfxaRtAeE4ff0GqZuV2Z19cu7)

**Comparison of two files (plain format):**

[![asciicast](https://asciinema.org/a/WqPl92c0Q4DwB1MUBNSL0awIs.svg)](https://asciinema.org/a/WqPl92c0Q4DwB1MUBNSL0awIs)

**Output the comparison in JSON format:**

[![asciicast](https://asciinema.org/a/hkkVLKw0FDQwaUhiIn502S0hi.svg)](https://asciinema.org/a/hkkVLKw0FDQwaUhiIn502S0hi)