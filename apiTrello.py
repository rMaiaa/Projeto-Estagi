import requests
import json as js

class trello:

    def __init__ (self):
        self.key = 'INSERT KEY'
        self.token = 'INSERT TOKEN'
        self.board = 'INSERT BOARD'


    def getBoard(self): #puxa os usuários que estão nas boards
        url = "INSERT URL THE BOARD" + self.board

        querystring = {"actions":"all","boardStars":"none","cards":"none","card_pluginData":"false","checklists":"none","customFields":"false","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","pluginData":"false","organization":"false","organization_pluginData":"false","myPrefs":"false","tags":"false","key":self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getCards(self):
        self.limit = '30'
        url = 'INSERT URL THE BOARD' + self.board + '/cards/?limit=' + self.limit + '&fields=name&members=true&member_fields=fullName&key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        
        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(type(dic))
        print(dic[0])
        print(dic[1])
        print(dic[2])
        print(dic[3]) # ->> 4º card
        print(dic[20])
        return str(dic[3]) #está retornando os dados do 4º card 
        

    def getCardID(self):
        self.idCard = 'INSERT ID CARD'
        
        url = 'INSERT URL THE BOARD' + self.board + '/cards/' + self.idCard + '?key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)
        
    def getMember(self):
        self.member = 'INSERT MEMBER'

        url = "INSERT API MEMBER" + self.member

        querystring = {"boardBackgrounds":"none","boardsInvited_fields":"name,closed,idOrganization,pinned","boardStars":"false","cards":"none","customBoardBackgrounds":"none","customEmoji":"none","customStickers":"none","fields":"all","organizations":"none","organization_fields":"all","organization_paid_account":"false","organizationsInvited":"none","organizationsInvited_fields":"all","paid_account":"false","savedSearches":"false","tokens":"none","key": self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)