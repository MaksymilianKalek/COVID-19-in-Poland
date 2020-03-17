import requests
from bs4 import BeautifulSoup
import time
from playsound import playsound

URL = "https://www.worldometers.info/coronavirus/"

infected_already = 0
deaths_already = 0

while True:
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    data = []
    table = soup.find("tbody")
    if table is None:
        continue

    rows = table.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    
    data.sort(key=lambda x:x[0])

    infected_new = int(data[117][1])
    deaths_new = int(data[117][3])

    if infected_already < infected_new:
        print(f"\nThere are {infected_new-infected_already} new cases. Totally there are {infected_new} people infected and {data[117][3]} have already died")
        playsound("eventually.mp3")
        infected_already = int(data[117][1])
        
        if deaths_already < deaths_new:
            print(f"There are {deaths_new-deaths_already} new deaths")
            playsound("death.mp3")
            deaths_already = int(data[117][3])
    else:
        print(f"\nThere aren't any new cases. Current statistics are: Total cases: {data[117][1]}, Lately announced cases: {data[117][2][1:]}, Total deaths: {data[117][3]}, Lately announced deaths: {data[117][4][1:]}")
        current = int(data[117][1])

    time.sleep(10)