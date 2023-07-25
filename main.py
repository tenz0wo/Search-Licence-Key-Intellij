import requests

with open("main.txt", "r") as f:
    urls = f.readlines()  
    
    for url in urls:
        try:
            response = requests.get(url=url, timeout=2)
            response.raise_for_status()  
            
            print("[!] Status Code: ", response.status_code, "Url: ", url)
            
            
        except requests.exceptions.RequestException as e:        
            print("[!] Error:", e)
