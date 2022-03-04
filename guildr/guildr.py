import requests
import json
from bs4 import BeautifulSoup
from lxml import etree

class Client:

    def __init__(self):

        self.session = requests.Session()
        headers = {
                    'authority': 'www.guilded.gg',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'content-type': 'application/json',
                    'cookie': '',
                    'guilded-client-id': '736740a4-b25c-4c77-b24e-901ee15e5ff7',
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


    def login(self, email, password):

        payload = {
        'email': f'{email}',
        'getMe': 'true',
        'password': f'{password}'}

        response = self.session.post('https://www.guilded.gg/api/login', json = payload)
        cookies = self.session.cookies.get_dict()
        gk = cookies['gk']
        guilded_mid = cookies['guilded_mid']
        guilded_ipah = cookies['guilded_ipah']
        authenticated = cookies['authenticated']
        hmac_signed_session = cookies['hmac_signed_session']
        newCookies = {'cookie': f'guilded_mid={guilded_mid}; guilded_ipah={guilded_ipah}; gk={gk}; hmac_signed_session={hmac_signed_session}; authenticated={authenticated}'}
        self.session.headers.update(newCookies)

        if response.status_code == 200:
            return True, json.loads(response.text)
        else:
            return False, json.loads(response.text)


    def getUserID(self):

        response = self.session.get('https://www.guilded.gg/api/users/me/teams/status')
        userID = json.loads(response.text)

        return userID['userId']


    def getTeamRoleIds(self):

        response = self.session.get('https://www.guilded.gg/api/me?isLogin=false&v2=true')
        userData = json.loads(response.text)

        return userData['teams'][0]['roleIds'][0]


    def getServerHomeID(self):

        response = self.session.get('https://www.guilded.gg/api/me?isLogin=false&v2=true')
        userData = json.loads(response.text)

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

        response = self.session.post(f'https://www.guilded.gg/api/teams/{self.getServerHomeID()}/groups', json = payload)

        return response, json.loads(response.text)


    def leaveGuild(self, guildID):

        response = self.session.put(f'https://www.guilded.gg/api/teams/{self.getServerHomeID()}/groups/{guildID}/membership/left')

        return response, json.loads(response.text)


    def archiveGuild(self, guildID):

        response = self.session.put(f'https://www.guilded.gg/api/teams/{self.getServerHomeID()}/groups/{guildID}/archive')

        return response, json.loads(response.text)


    def deleteGuild(self, guildID):

        response = self.session.delete(f'https://www.guilded.gg/api/teams/{self.getServerHomeID()}/groups/{guildID}')

        return response, json.loads(response.text)


    def changeName(self, name):

        payload = {
        'name': name,
        'userId': self.getUserID()}

        response = self.session.put(f'https://www.guilded.gg/api/users/{self.getUserID()}/profilev2', json = payload)

        return response, json.loads(response.text)


    def changeTagline(self, tagline):

        payload = {
        'aboutInfo': {
            'tagLine': tagline},
        'userId': self.getUserID()}

        response = self.session.put(f'https://www.guilded.gg/api/users/{self.getUserID()}/profilev2', json = payload)

        return response, json.loads(response.text)


    def changePFP(self, pfp):

        payload = {
        'imageUrl': pfp}

        response = self.session.post(f'https://www.guilded.gg/api/users/me/profile/images', json = payload)

        return response, json.loads(response.text)
