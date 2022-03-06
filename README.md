
# Guildr
[![MIT License](https://img.shields.io/github/last-commit/akimbo7/Guildr?color=%23533B4D&style=flat-square)](https://github.com/akimbo7/Guildr)
[![MIT License](https://img.shields.io/github/repo-size/akimbo7/Guildr?color=%23F564A9&style=flat-square)](https://github.com/akimbo7/Guildr)
[![MIT License](https://img.shields.io/github/v/release/akimbo7/Guildr?color=%23fbe3c5&style=flat-square)](https://github.com/akimbo7/Pirtul/releases)

![Logo](https://cdn.discordapp.com/attachments/935638977707376674/949768919755943946/New_Project_4.png)

A simple API Wrapper for Guilded.

*Frequently updated!*

I am not a user of Guilded, meaning I do not keep track of new Guilded updates or patches. If a function stops working as a result of this, feel free to open an issue.

Enjoy :)


## Installation

```
python3 -m pip install --user --upgrade git+https://github.com/akimbo7/Guildr.git#egg=guildr
```

**Requirements**:

- bs4 >= 0.0.1
- colorama >= 0.4.4
- lxml >= 4.8.0
- requests >= 2.27.1
- uuid >= 1.30

## Remove

```
python3 -m pip uninstall git+https://github.com/akimbo7/Guildr.git#egg=guildr
```

## Example Usage

```python
import guildr

client = guildr.Client(log=True)

email = 'johnsmith01@gmail.com'
password = 'Password123'

#returns True or False along with the json response
x = client.login(email = email, password = password)

userID = client.getUserID()
print(f'User ID: {userID}')
```

Check out the full feature list [here] (https://github.com/akimbo7/Guildr/blob/main/usage/USAGE.md)
