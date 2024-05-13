from multiprocessing.dummy import Array
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re


url = "https://weather.com/weather/today/l/49.99,36.23?par=google"
r = requests.get(url)
print(r.status_code)
soup = bs(r.text, 'html.parser')
F = soup.find('span', class_="CurrentConditions--tempValue--MHmYY")
P = soup.find('div', class_="CurrentConditions--phraseValue--mZC_p")
print("In Kharkiv: " + F.text + " fahrenheit" + ", " + P.text)

  
