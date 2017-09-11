import sys
import requests
from bs4 import BeautifulSoup
import time
import random

# Beautiful soup would be better

all_emails = []

for i in range(26):
    letter = chr(i+65)
    url = "https://mwsu.edu/profiles/people.asp?browse="+letter
    print(url)
    html = requests.get(url).text.split('\n')
    
    for line in html:
        found = line.find('href="mailto:')
        
        if found > 0:
            line = line[found:]
            pos = line.find('">')

            all_emails.append(line[pos+2:-4])
    
    time.sleep(random.randint(0,3))

print(all_emails)
