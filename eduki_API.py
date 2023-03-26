import requests
import json
from datetime import date

limit = 10000
offset = 0
subject_list = ["Mathe", "Deutsch", "Kunst", "Kita", "Englisch", "Erdkunde", "Sachunterricht"]
subject = subject_list[0]

url = "https://api.eu.detectum.com/lehrermarktplatz/search/search_plain"
querystring = {f"param_1":"author","id_1":"","order":"","limit":f"{str(limit)}","offset":f"{str(offset)}","q":f"{subject}", "world": "de"}
payload = ""
headers = {
    "authority": "api.eu.detectum.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://eduki.com",
    "referer": "https://eduki.com/de/suchergebnisse?query=Deutsch",
    "sec-ch-ua": "^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

r = requests.get(url, data=payload, headers=headers, params=querystring)
r_data = r.json()

with open(f'{subject}_{limit}_{date.today()}.json', 'w') as j:
    json.dump(r_data, j, indent=2)