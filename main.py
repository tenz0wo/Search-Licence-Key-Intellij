import requests

POSSIBLE_URLS = []

with open("main.txt", "r") as f:
    urls = f.readlines()  
    
    for url in urls:
        try:
            response = requests.get(url=url, timeout=2)
            response.raise_for_status()  
            POSSIBLE_URLS.append(url.strip("\n"))
        except requests.exceptions.RequestException as e:        
            ...

for pos in POSSIBLE_URLS:
    print("[!] Possible Url :", pos)
