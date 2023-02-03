import os, marshal
os.system("pip install pyfiglet")
os.system("pip install stepic")
os.system("pip install eyed3")
os.system("pip install Pillow")
os.system("pip install termcolor")
import pyfiglet
from eyed3 import load
from stepic import encode
from stepic import decode
from PIL import Image
from termcolor import colored
g = '\033[01;32m'
r = '\033[01;31m'
y = '\033[01;33m'


def Banner():
    print (f"""
    {y}
    the writer : EsfeLurM
    
    Channel Telegram : https://t.me/esfelurm
    
    GitHub : github.com/esfelurm
    
    
    {r}[{y}1{r}] {g}Hide information in {r}music
    
    {r}[{y}2{r}] {g}Extracting information from {r}music 
    
    {r}[{y}3{r}] {g}Hide information in {r}photos [{y}Format .png{r}]
    
    {r}[{y}4{r}] {g}Extract information from {r}photos [{y}Format .png{r}] 
    
    """)
os.system("clear")
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00sP\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x02l\x01m\x02Z\x02\x01\x00d\x00d\x03l\x03m\x04Z\x04\x01\x00d\x00d\x04l\x03m\x05Z\x05\x01\x00d\x00d\x05l\x06m\x07Z\x07\x01\x00d\x00d\x01l\x03Z\x03d\x00d\x06l\x08m\tZ\t\x01\x00d\x01S\x00)\x07\xe9\x00\x00\x00\x00N)\x01\xda\x04load)\x01\xda\x06encode)\x01\xda\x06decode)\x01\xda\x05Image)\x01\xda\x07colored)\nZ\x08pyfigletZ\x05eyed3r\x02\x00\x00\x00Z\x06stepicr\x03\x00\x00\x00r\x04\x00\x00\x00Z\x03PILr\x05\x00\x00\x00Z\ttermcolorr\x06\x00\x00\x00\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xda\x00\xda\x08<module>\x01\x00\x00\x00s\x0e\x00\x00\x00\x08\x00\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x08\x01\x10\x01'))

Banner()

Number = int(input(f"{y}Enter Number :{g} "))

def Encode_m():
    try:
        os.system("clear")
    except:
        os.system("cls")
    print (colored(pyfiglet.figlet_format('Music encode', font = 'banner3-D'), 'green'))
    data = input(f"{g}Enter your desired text >{r} ")
    audio = input(f"{r}[{y}?{r}]{g} Give the name and path of the music : ")
    img_name = input(f"{r}[{y}?{r}]{g} Image File : ")
    audio = load(audio) 
    img = Image.open(img_name)
    img_steg = encode(img , data.encode())
    img_steg.save(img_name) 

    audio.initTag()
    audio.tag.images.set(3 , open(img_name,"rb").read() , "image/png")
    audio.tag.save(), print(f"{g}it is finished !")
    
def Decode_m():
    try:
        os.system("clear")
    except:
        os.system("cls")
    print (colored(pyfiglet.figlet_format('Music decode', font = 'banner3-D'), 'red'))
    audio = input(f"{r}[{y}?{r}]{g} Give the name and path of the music : ")
    audio = load(audio)

    img = open("temp_img.png", "wb")
    img.write(audio.tag.images[0].image_data)
    img.close()
    img = Image.open("temp_img.png")
    text = decode(img)
    print("Data : {}".format(text))
    
def Encode_p():
    try:
        os.system("clear")
    except:
        os.system("cls")
    print (colored(pyfiglet.figlet_format('Encode photo', font = 'banner3-D'), 'green'))
    file  = input(f"{r}[{y}?{r}]{g} Image File : ")
    img = Image.open(file)
    text = input(f"{g}[+] Text inside the photo :{y} ")
    img_stegano = encode(img,text.encode())  
    name = input("Output Name : ")
    img_stegano.save(name)
    
def Decode_p():
    try:
        os.system("clear")
    except:
        os.system("cls")
    print (colored(pyfiglet.figlet_format('decode photo', font = 'banner3-D'), 'green'))
    file = input(f"{r}[{y}?{r}]{g} Image File : ")
    img = Image.open(file)
    Decoded = decode(img)
    print(f"{g}[+] Text inside the photo :{y} "+Decoded)

if Number == 1:
    Encode_m()
elif Number == 2:
    Decode_m()
elif Number == 3:
    Encode_p()
elif Number == 4:
    Decode_p()
# Amir Esfelurm
