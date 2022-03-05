import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import uuid
from colorama import *; init()

class Client:

    def __init__(self, log=False):

        self.log = log

        self.session = requests.Session()
        headers = {
                    'authority': 'www.guilded.gg',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'content-type': 'application/json',
                    'guilded-client-id': f'{uuid.uuid1()}',
                    'origin': 'https://www.guilded.gg',
                    'referer': 'https://www.guilded.gg/',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"macOS"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                    }
        self.session.headers.update(headers)
        self.session.get('https://www.guilded.gg/')

        #self.login(email, password) ---> NEED TO GET THIS TO WORK, I'M DUMB SO I HAVE NO CLUE HOW TO

    def logging(self, type, text):

        dict = {
            'get': Fore.BLUE,
            'post': Fore.RED,
            'put': Fore.YELLOW,
            'delete': Fore.GREEN}

        color = dict.get(type)
        print(f'{color}{text}{Fore.RESET}')


    def login(self, email=None, password=None):

        payload = {
        'email': f'{email}',
        'getMe': 'true',
        'password': f'{password}'}

        response = self.session.post('https://www.guilded.gg/api/login', json = payload)
        if response.status_code != 200:
            return response.json()
        cookies = self.session.cookies.get_dict()
        gk = cookies['gk']
        guilded_mid = cookies['guilded_mid']
        guilded_ipah = cookies['guilded_ipah']
        authenticated = cookies['authenticated']
        hmac_signed_session = cookies['hmac_signed_session']
        newCookies = {'cookie': f'guilded_mid={guilded_mid}; guilded_ipah={guilded_ipah}; gk={gk}; hmac_signed_session={hmac_signed_session}; authenticated={authenticated}'}
        self.session.headers.update(newCookies)

        if self.log:
            self.logging('post', response.json())

        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.json()


    def logout(self):

        response = self.session.post('https://www.guilded.gg/api/logout')

        if self.log:
            self.logging('post', response.json())

        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.json()

    def getUserID(self):

        response = self.session.get('https://www.guilded.gg/api/users/me/teams/status')

        if self.log:
            self.logging('get', response.json())

        if response.status_code != 200:
            return response.json()
        userID = response.json()

        return userID['userId']


    def getTeamRoleIds(self):

        response = self.session.get('https://www.guilded.gg/api/me?isLogin=false&v2=true')

        if self.log:
            self.logging('get', response.json())

        if response.status_code != 200:
            return response.json()
        userData = response.json()

        return userData['teams'][0]['roleIds'][0]


    def getHomeServerID(self):

        response = self.session.get('https://www.guilded.gg/api/me?isLogin=false&v2=true')

        if self.log:
            self.logging('get', response.json())

        if response.status_code != 200:
            return response.json()
        userData = response.json()

        return userData['teams'][0]['id']


    def createGuild(self, serverName, isPublic):

        payload = {
                'avatar': None,
                'description': "",
                'isBase': 'false',
                'isPublic': isPublic,
                'visibilityTeamRoleId': self.getTeamRoleIds(),
                'membershipTeamRoleId': self.getTeamRoleIds(),
                'name': serverName,
                'userIds': 'null',
                'users': []}

        response = self.session.post(f'https://www.guilded.gg/api/teams/{self.getHomeServerID()}/groups', json = payload)

        if self.log:
            self.logging('post', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def leaveGuild(self, guildID):

        response = self.session.put(f'https://www.guilded.gg/api/teams/{self.getHomeServerID()}/groups/{guildID}/membership/left')

        if self.log:
            self.logging('put', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def archiveGuild(self, guildID):

        response = self.session.put(f'https://www.guilded.gg/api/teams/{self.getHomeServerID()}/groups/{guildID}/archive')

        if self.log:
            self.logging('put', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def deleteGuild(self, guildID):

        response = self.session.delete(f'https://www.guilded.gg/api/teams/{self.getHomeServerID()}/groups/{guildID}')

        if self.log:
            self.logging('delete', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def changeName(self, name):

        payload = {
        'name': name,
        'userId': self.getUserID()}

        response = self.session.put(f'https://www.guilded.gg/api/users/{self.getUserID()}/profilev2', json = payload)

        if self.log:
            self.logging('put', response.json())

        if response.status_code != 200:
            return response, response.json()

        return response, response.json()


    def changeTagline(self, tagline):

        payload = {
        'aboutInfo': {
            'tagLine': tagline},
        'userId': self.getUserID()}

        response = self.session.put(f'https://www.guilded.gg/api/users/{self.getUserID()}/profilev2', json = payload)

        if self.log:
            self.logging('put', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def changePFP(self, pfp):

        payload = {
        'imageUrl': pfp}

        response = self.session.post(f'https://www.guilded.gg/api/users/me/profile/images', json = payload)

        if self.log:
            self.logging('post', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def changeStatus(self, status):#, clearAfter):

        #self.clearAfter = 0

        payload = {"content":{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":status,"marks":[]}]}]}]}},"customReactionId":90001865,"expireInMs":0}

        response = self.session.post(f'https://www.guilded.gg/api/users/me/status', json = payload)

        if self.log:
            self.logging('post', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def sendFriendRequest(self, userID):

        payload = {"friendUserIds":[f"{userID}"]}

        response = self.session.post('https://www.guilded.gg/api/users/me/friendrequests', json = payload)

        if self.log:
            self.logging('post', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def sendMessage(self, channelID, message, isSilent, isPrivate):

        payload = {"messageId":f"{uuid.uuid1()}","content":{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":message,"marks":[]}]}]}]}},"repliesToIds":[],"confirmed":False,"isSilent":isSilent,"isPrivate":isPrivate}

        response = self.session.post(f'https://www.guilded.gg/api/channels/{channelID}/messages', json = payload)

        if self.log:
            self.logging('post', response.json())

        if response.status_code != 200:
            return response.json()

        return response, response.json()


    def sendDM(self, targetID, message):

        payload = {"users":[{"id":targetID}]}

        response1 = self.session.post(f'https://www.guilded.gg/api/users/{self.getUserID()}/channels', json = payload)

        if self.log:
            self.logging('post', response.json())

        channelID = response1.json()['channel']['id']

        payload = {"messageId":f"{uuid.uuid1()}","content":{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":message,"marks":[]}]}]}]}},"repliesToIds":[],"confirmed":False,"isSilent":False,"isPrivate":False}

        response2 = self.session.post(f'https://www.guilded.gg/api/channels/{channelID}/messages', json = payload)

        if self.log:
            self.logging('post', response2.json())

        return response2, response2.json()


    def register(self, username, email, password):
        pass
        #payload = {"extraInfo":{"platform":"desktop"},"name":username,"email":email,"password":password,"fullName":username}

        #response = requests.post(f'https://www.guilded.gg/api/users?type=email', json = payload)
        #print(response.json())
        #userID = (response.json())['user']['id']

        #payload = {"extraInfo":{"platform":"desktop"},"userId":userID,"teamName":f"{username} server"}

        #response = requests.post(f'https://www.guilded.gg/api/teams', json = payload)
        #print(response.json())
