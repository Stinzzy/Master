import requests

URL = "https://api.chucknorris.io/jokes/random"

try:
    r = requests.get(URL, timeout=5)
    if r.status_code == 200:
        data = r.json()
        print(data.get("value", "vitsiä ei löytynyt"))
    else:
        print(f"Virhe: {r.status_code}")
except requests.exceptions.RequestException:
    print("hakua ei voitu thedä.")