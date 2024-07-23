import requests
from requests.auth import HTTPProxyAuth
import warnings

warnings.filterwarnings('ignore')

print("You must setup proxy config.")
print("At the moment, we only accept brightdata proxies.")
print("Go open a free trial account on brightdata. ")
print("")
proxy_username = input("Enter your brightdata proxy's username: ")
proxy_pass = input("Enter your brightdata proxy's password: ")

proxy = {
    "http": f"http://{proxy_username}:{proxy_pass}@brd.superproxy.io:22225",
    "https": f"http://{proxy_username}:{proxy_pass}@brd.superproxy.io:22225"
}

proxy_auth = HTTPProxyAuth(f'{proxy_username}', f'{proxy_pass}')

def check_username(username):
    url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"

    payload = {"username": username}
    headers = {
    "accept": "*/*",
    "accept-language": "es-ES,es;q=0.9",
    "content-type": "application/json",
    "cookie": "__dcfduid=71ef5db0482f11ef8bb5157e9cc557fd; __sdcfduid=71ef5db1482f11ef8bb5157e9cc557fdc165e5dcc41a2c7b73a80464d9cc9d3d872fd9de4c4fe97d10a01605e2f310ab; __cfruid=a416afd09a7704dbcf9c53ac0d9b40a771736753-1721655408; _cfuvid=0kGUOmSKse6wHK7gHXRGeKVy395GZiedLQcnMfP2t.4-1721655408404-0.0.1.1-604800000; locale=es-ES; cf_clearance=zdmHfwFx2zgT.2zxSLL2k4aL0d5BFx_nNMqUMBQqGDo-1721655412-1.0.1.1-pveAoyjnuyLGJ4TYyMh2jhbJTIPeimSr1qEv5T_sRbmdyU.XVG1yZAzS367onG.gdAmlKxxUxoWoLNqSU01bmw",
    "origin": "https://discord.com",
    "priority": "u=1, i",
    "referer": "https://discord.com/register",
    "sec-ch-ua": "Not/A;Brand",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "es-ES",
    "x-discord-timezone": "Europe/Madrid",
    "x-fingerprint": "1264939221693763594.ZlwQPsqUrpw0qcus0AFGozd74lo",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzLUVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzEwOTI3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }


    try:
        response = requests.post(url, json=payload, headers=headers, proxies=proxy, auth=proxy_auth, verify=False)
        response_data = response.json()
        try:
            return response_data['taken']
        except:
            return "ratelimit"
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "requesterror"
