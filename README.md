
# Guildr
[![MIT License](https://img.shields.io/github/last-commit/akimbo7/Guildr?color=%23533B4D&style=flat-square)](https://github.com/akimbo7/Guildr)
[![MIT License](https://img.shields.io/github/repo-size/akimbo7/Guildr?color=%23F564A9&style=flat-square)](https://github.com/akimbo7/Guildr)
[![MIT License](https://img.shields.io/github/repo-size/akimbo7/Guildr?color=%23FAE3C6&style=flat-square)](https://github.com/akimbo7/Pirtul/releases)

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


## Features
`Initializing your client`
```python
client = guildr.Client()
```

This initializes a client for Portal usage.

**Parameters**:
- log - Defaults to False

**Returns**:
- A guildr client

#
`Logging in`
```python
client.login(email = 'Your email', password = 'Your password')
```

This logs you into a given account.

**Parameters**:
- email
- password

**Returns**:
- True - If login was **successful**
- False - If login was **unsuccessful**
- Json response

#
`Logging out`
```python
client.logout()
```

This logs you out of the current account. When logging out, Guilded relys on the current cookies to log out an account. To have a successful log out, make sure your cookies and updated.

**Parameters**:
- None

**Returns**:
- True - If logout was **successful**
- False - If logout was **unsuccessful**
- Json response

#
`Get the users ID`
```python
client.getUserID()
```

This gets the user ID of the current account.

**Parameters**:
- None

**Returns**:
- The user's ID if successful
- The Json response if unsuccessful

#
`Get the users team role IDs`
```python
client.getTeamRoleIDs()
```

This gets the team role IDs of the current account.

**Parameters**:
- None

**Returns**:
- The user's team role ID if successful
- The Json response if unsuccessful

#
`Get the users home server ID`
```python
client.getHomeServerID()
```

This gets the home server ID of the current account.

**Parameters**:
- None

**Returns**:
- The user's home server ID if successful
- The Json response if unsuccessful

#
`Create a guild`
```python
client.createGuild(serverName = 'Name of server', isPublic = True)
```

This creates a guild.

**Parameters**:
- serverName - The name of the server
- isPublic - If the guild should be public or not (Defaults to True)

**Returns**:
- Json response

#
`Leave a guild`
```python
client.leaveGuild(guildID = 'ID of guild')
```

This leaves a guild.

**Parameters**:
- guildID - ID of the guild to leave

**Returns**:
- Json response

#
`Archive a guild`
```python
client.archiveGuild(guildID = 'ID of guild')
```

This archives a guild.

**Parameters**:
- guildID - ID of the guild to archive

**Returns**:
- Json response

#
`Delete a guild`
```python
client.deleteGuild(guildID = 'ID of guild')
```

This deletes a guild.

**Parameters**:
- guildID - ID of the guild to delete

**Returns**:
- Json response

#
`Change name`
```python
client.changeName(name = 'New username')
```

This changes the current accounts username.

**Parameters**:
- name - New username to change to

**Returns**:
- Json response

#
`Change tag line`
```python
client.changeTagLine(tagline = 'New tagline')
```

This changes the current accounts tagline.

**Parameters**:
- tagline - New tagline to change to

**Returns**:
- Json response

#
`Change profile picture`
```python
client.changePFP(pfp = 'location/of/image')
```

This changes the current accounts profile picture.

**Parameters**:
- pfp - New picture to change to

**Returns**:
- Json response

#
`Change status`
```python
client.changeStatus(status = 'New status')
```

This changes the current accounts status.

**Parameters**:
- status - New status to change to

**Returns**:
- Json response

#
`Use legacy mode`
```python
client.useLegacyMode(use = True)
```

This changes the accounts layout to legacy mode.

**Parameters**:
- use - True of False (Defaults to False)

**Returns**:
- Json response

#
`Send friend request`
```python
client.sendFriendRequest(userID = 'ID of user to request')
```

This sends a friend request to a given user ID.

**Parameters**:
- userID - ID of the user to send a friend request to

**Returns**:
- Json response

#
`Send a channel message`
```python
client.sendMessage(channelID = 'ID of channel', message = 'Message to send', isSilent = False, isPrivate = False)
```

This sends a message to a given channel.

**Parameters**:
- channelID - ID of the channel to send a message in
- message - Message to send in channel
- isSilent - If the message sent should ping the user (Defaults to False)
- isPrivate - If the message sent should be sent privately (Defaults to False)

**Returns**:
- Json response

#
`Send a DM`
```python
client.sendDM(targetID = 'ID of user to send DM to', message = 'Message to DM')
```

This sends a DM to a given user.

**Parameters**:
- targetID - ID of a user to send the dm to
- message - Message to send to the user

**Returns**:
- Json response

#
`Create an account` - *soon*
```python
client.register(username = 'Username', email = 'Email', password = 'Password')
```

This creates an account.

**Parameters**:
- username - Username of the account 
- email - Email of the account
- password - Password of the account

**Returns**:
- Json response
