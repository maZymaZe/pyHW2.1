import requests
from show_data import show_data
def web():
    url = "https://raw.githubusercontent.com/maZymaZe/pyHW/master/data.txt"    
    r = requests.get(url)
    with open("data.txt","wb") as f:  
        f.write(r.content)
    show_data()
    