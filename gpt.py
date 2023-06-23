from requests import get
import json, time
from os import system as sys
from random import randint
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
def clear():
    try:sys("clear")
    except:sys("cls")


w = input(f"""
{lrd}[{lgn}~{lrd}]{lgn} Written by : {yw}@Esfelurm  {lrd}[{lgn}~{lrd}]{lgn} Web service used : {yw}Haji Web Service

{lgn}Version : {lrd}1.0.1

{lrd}[{lgn}1{lrd}]{lgn} asking questions - {lrd}[{lgn}2{lrd}]{lgn} photo search \n{lrd}[{lgn}3{lrd}]{lgn} Proxy (Update for Telegram) - {lrd}[{lgn}4{lrd}]{lgn} logo maker

Enter : """)

def question():
    question = input(f"\n{lrd}[{lgn}+{lrd}]{lgn} Ask your question : {cn}")
    url = f"https://api2.haji-api.ir/gpt/gpt.php?text={question}"
    response = get(url)
    print (f"\n{pe}Your question has been answered\n{yw}-------------------------- {lgn}")
    for char in json.loads(response.text)["result"]["answer"]:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print (f"\n\n{yw}-------------------------- ")

def photo_s():
    question = input(f"\n{lrd}[{lgn}+{lrd}]{lgn} Give me the name, or a subject of the photo and I will download the photo for you :{cn} ")
    url = f"https://haji-api.ir/prompts/?text={question}"
    response = get(url)
    Ye = json.loads(response.text)["result"]
    print (f"\n{lrd}[{lgn}%{lrd}]{lgn} Number of photos found {yw}: ",len(Ye))
    Num = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Do you want to download photos [Y/N] : ")
    File = input(f"{lrd}[{lgn}?{lrd}]{lgn} Enter the path where you want the photos to be saved : {cn}")
    if Num == 'y' or 'Y':
        for I in Ye:
            try:f = get(I)
            except:pass            
            s = randint(0,30)
            filename = File+f"/image{s}.jpg"
            try:
                with open(filename, "wb") as h:
                    h.write(f.content)
                    print (f"\n{lrd}[{lgn}+{lrd}]{lgn} A picture has been downloaded ! : {gn}{filename}")
            except:print (f"{lrd}Enter the correct path !")
    else:
    	print ("Bye Bye")
def proxy():
    res = get('https://haji-api.ir/proxy')
    if res.status_code == 200:
        data = json.loads(res.text)["Result"]
        print ("It will be downloaded in 5 seconds ")
        time.sleep(5)
        for item in data:
            print (f"{yw}---------------------------")
            print(f'{lgn}Server {pe}: {lrd}{item["server"]} \n{lgn}Port{pe} : {lrd}{item["port"]} \n{lgn}secret{pe} : {lrd}{item["secret"]}')
            print (f"{yw}---------------------------")
            time.sleep(1)
    else:
        print(f"\n {lrd}Failed to get data. Error code: {res.status_code} ")
def Logo():
    txt = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Issue : ")
    type = input(f"""{lgn}
neon-logo {lrd}|{lgn} booking-logo {lrd}|{lgn} comics-logo
water-logo {lrd}|{lgn} fire-logo {lrd}|{lgn} clan-logo {lrd}|{lgn} my-love-logo
blackbird-logo {lrd}|{lgn} smurfs-logo {lrd}|{lgn} style-logo
runner-logo {lrd}|{lgn} fluffy-logo
glow-logo {lrd}|{lgn} crafts-logo {lrd}|{lgn} fabulous-logo
amped-logo {lrd}|{lgn} graffiti-logo {lrd}|{lgn} graffiti-burn-logo
star-wars-logo {lrd}|{lgn} graffiti-3d-logo {lrd}|{lgn} scribble-logo
chrominium-logo {lrd}|{lgn} harry-potter-logo {lrd}|{lgn} world-cup-2014-logo
heavy-metal-logo {lrd}|{lgn} thanksgiving1-logo {lrd}|{lgn} april-fools-logo
beauty-logo {lrd}|{lgn} winner-logo
silver-logo {lrd}|{lgn} steel-logo {lrd}|{lgn} global-logo
inferno-logo {lrd}|{lgn} birdy-logo {lrd}|{lgn} roman-logo
minions-logo {lrd}|{lgn} superfit-logo {lrd}|{lgn} fun-and-play-logo
brushed-metal-logo {lrd}|{lgn} birthday-fun-logo {lrd}|{lgn} colored2-logo
swordfire-logo {lrd}|{lgn} flame-logo {lrd}|{lgn} wild-logo {lrd}|{lgn}
street-sport-logo {lrd}|{lgn} surfboard-white-logo {lrd}|{lgn}
amazing-3d-logo {lrd}|{lgn} flash-fire-logo {lrd}|{lgn} uprise-logo {lrd}|{lgn}
sugar-logo {lrd}|{lgn} robot-logo {lrd}|{lgn} genius-logo {lrd}|{lgn}
cereal-logo {lrd}|{lgn} kryptonite-logo {lrd}|{lgn} patriot-logo {lrd}|{lgn}
holiday-logo {lrd}|{lgn} sports-logo {lrd}|{lgn} thanksgiving2-logo {lrd}|{lgn}
trance-logo {lrd}|{lgn} spider-men-logo {lrd}|{lgn} theatre-logo {lrd}|{lgn}
vintage-racing-logo {lrd}|{lgn} ninja-logo {lrd}|{lgn} bumblebee-logo {lrd}|{lgn}
vampire-logo {lrd}|{lgn} sunrise-logo {lrd}|{lgn} monsoon-logo {lrd}|{lgn}
strongman-logo {lrd}|{lgn} game-over-logo {lrd}|{lgn}
    
    
{lrd}[{lgn}?{lrd}]{lgn} Logo type : """)
    max = input(f"\n{lrd}[{lgn}?{lrd}]{lgn}Desired size [0/200] : ")
    Color = input(f"\n{lrd}[{lgn}?{lrd}]{lgn}Logo color : ")
    url = f"https://api.irateam.ir/Logo-Maker/?text={txt}&script={type}&fontsize={max}&textcolor={Color}"
    response = get(url)
    clear()
    time.sleep(2)
    print (f"\n{lgn}Issue : {lrd}{txt}\n{lgn}Logo type : {lrd}{type}\n{lgn}image size : {max}\nPhoto color : {Color}")
    Num = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Do you want to download photos [Y/N]")
    File = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Enter the path where you want the photos to be saved : {cn}")
    try:f = get(url)
    except:print ("Connection error " )          
    s = randint(0,30)
    filename = File+f"/image{s}.jpg"
    try:
        with open(filename, "wb") as h:
            h.write(f.content)
            print (f"\n{lrd}[{lgn}+{lrd}]{lgn} A picture has been downloaded ! : {gn}{filename}")
    except:print (f"{lrd}Enter the correct path !")
while True:
    if w == '1':
        question()
        Cl = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Do you want to continue {lrd}[{lgn}Y{yw}/{rd}N{lrd}] : {cn}")
        if Cl == 'y' or Cl == 'Y':
            clear()
        else:
        	break
    if w == '2':
        photo_s()
        Cl = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Do you want to continue {lrd}[{lgn}Y{yw}/{rd}N{lrd}] : {cn}")
        if Cl == 'y' or Cl == 'Y':
            clear()
        else:
        	break
    if w == '3':
        proxy()
        Cl = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Do you want to continue {lrd}[{lgn}Y{yw}/{rd}N{lrd}] : {cn}")
        if Cl == 'y' or Cl == 'Y':
            clear()
        else:
        	break
    if w == '4':
        Logo()
        Cl = input(f"\n{lrd}[{lgn}?{lrd}]{lgn} Do you want to continue {lrd}[{lgn}Y{yw}/{rd}N{lrd}] : {cn}")
        if Cl == 'y' or Cl == 'Y':
            clear()
        else:
        	break