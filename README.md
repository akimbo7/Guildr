# Guildr
[![MIT License](https://img.shields.io/github/last-commit/akimbo7/Guildr?color=%23533B4D&style=flat-square)](https://github.com/akimbo7/Guildr)
[![MIT License](https://img.shields.io/github/repo-size/akimbo7/Guildr?color=%23F564A9&style=flat-square)](https://github.com/akimbo7/Guildr)
[![MIT License](https://img.shields.io/github/repo-size/akimbo7/Guildr?color=%23FAE3C6&style=flat-square)](https://github.com/akimbo7/Pirtul/releases)

A simple API Wrapper for Guilded.


## Installation

```
python3 -m pip install --user --upgrade git+https://github.com/akimbo7/Guildr.git#egg=guildr
```

**Requirements**:

- requests >= 2.27.1
- bs4 >= 0.0.1
- lxml >= 4.8.0

## Remove

```
python3 -m pip uninstall git+https://github.com/akimbo7/Guildr.git#egg=guildr
```

## Example Usage

```python
import guildr

client = guildr.Client()

email = 'johnsmith01@gmail.com'
password = 'Password123'

#returns True or False along with the json response
x = client.login(email, password)

userID = client.getUserID()
print(f'User ID: {userID}')
```
