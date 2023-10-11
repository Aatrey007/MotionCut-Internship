import requests 
from bs4 import Beautifulsoup
import json
req = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 
soup = Beautifulsoup(req.content,"html.parser")
print(soup.get_text)
