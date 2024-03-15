import requests 


def getAllPets():
    return requests.request(method="GET", url="https://biggamesapi.io/api/collection/Pets", data={}, headers = {}).text


def getTopClans(PageSize):
    return requests.request("GET", url=f"https://biggamesapi.io/api/clans?page=1&pageSize={PageSize}&sort=Points&sortOrder=desc", data={}, headers={}).text

def getClanData(clanTag):
    return requests.request("GET", f"https://biggamesapi.io/api/clan/{clanTag}", headers={}, data={}).text

def getCurrentBattle():
    return requests.request("GET", url="https://biggamesapi.io/api/activeClanBattle", headers={}, data={}).text




def format_value(value):
    reversed_value = str(value)[::-1]
    chunks = [reversed_value[i:i+3] for i in range(0, len(reversed_value), 3)]
    formatted_value = '.'.join(chunks)[::-1]
    return formatted_value

def getRAP(item):

    response = requests.get("https://biggamesapi.io/api/rap", headers={}, data={})
    data = response.json()


    for entry in data['data']:
        if entry['configData']['id'] == item:

            entry['value'] = format_value(entry['value'])
            return entry
    return None  


