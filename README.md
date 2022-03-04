# Guildr

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
