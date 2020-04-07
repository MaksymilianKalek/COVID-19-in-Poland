from requests import get
from bs4 import BeautifulSoup
import time
from playsound import playsound

URL = "https://www.worldometers.info/coronavirus/country/poland/"

current_dead = None
current_infected = None
current_recovered = None

while True:
    
    page = get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    def convert(num):
        num_list = list(num)
        if "," in num_list:
            num_list.remove(",")
        num = int("".join(num_list))
        return num

    div = soup.find_all("div", class_="maincounter-number")[0]
    num =  div.find("span").text.strip()
    convert(num)
    infected = num
    div = soup.find_all("div", class_="maincounter-number")[1]
    num = div.find("span").text.strip()
    convert(num)
    dead = num

    div = soup.find_all("div", class_="maincounter-number")[2]
    num = div.find("span").text.strip()
    convert(num)

    recovered = num

    if None in (infected, dead, recovered):
        continue
    
    if current_dead == current_infected == current_recovered == None:
        print("\n\n\n   XXXXXX    XXXXXX    X           X   X    XXXXXX                X   XXXXXX")
        print("  X         X      X    X         X    X    X     X             X X   X    X")
        print(" X         X        X    X       X     X    X      X           X  X   X    X")
        print(" X         X        X     X     X      X    X       X   XXXXX     X   XXXXXX")
        print(" X         X        X      X   X       X    X      X              X        X ")
        print("  X         X      X        X X        X    X     X               X        X")
        print("   XXXXXX    XXXXXX          X         X    XXXXXX                X        X\n\n\n")
        print(f" Welcome to COVID-19 in Poland notification system!\n")
        print(f" Currently there are infected: {infected}, dead: {dead}, recovered: {recovered} people in Poland\n")
        print(" You will get notified when there are new know statistics available")
        
        current_dead = dead
        current_infected = infected
        current_recovered = recovered

    if current_dead != dead:
        playsound("death.mp3")
        print(f" There are {dead - current_dead} new death cases confirmed")
        print(f" Totally {dead} people died in Poland due to COVID-19 outbreak")
        current_dead = dead

    if current_infected != infected:
        playsound("eventually.mp3")
        print(f" There are {infected - current_infected} new infected cases confirmed")
        print(f" Totally there are {infected} infected people in Poland")
        current_infected = infected
        
    if current_recovered != recovered:
        playsound("recover.mp3")
        print(f" There are {recovered - current_recovered} cases of recovery confirmed")
        print(f" Totally {recovered} people have recovered in Poland from COVID-19")
        current_recovered = recovered

    time.sleep(10)