import pyautogui
import time

def click(c):
    pyautogui.click(x=c[0],y=c[1])

def write(text):
    pyautogui.typewrite(text)

def enter():
    pyautogui.press("enter")

def scroll(val):
    pyautogui.scroll(val)

def sleep(val):
    time.sleep(val)

def find_click(img):
    res = pyautogui.locateOnScreen(img)
    edit_but = pyautogui.center(res)
    pyautogui.moveTo(edit_but)
    sleep(5)
    click(edit_but)

def find(img):
    res = pyautogui.locateOnScreen(img)
    edit_but = pyautogui.center(res)
    pyautogui.moveTo(edit_but)
    return edit_but

def search(url):
    find_click("1.png")
    sleep(5)
    write("ch")
    sleep(5)
    find_click("2.png")
    sleep(10)
    write(url)
    sleep(5)
    enter()

#links 
indice = "https://www.niftyindices.com/Factsheet/"
auto = "ind_nifty_auto.pdf"
bank = "ind_nifty_bank.pdf"
fin_serv = "ind_Nifty_Financial_Services.pdf"
fmcg = "ind_nifty_FMCG.pdf"
health = "Factsheet_Nifty_Healthcare_Index.pdf"
it = "ind_nifty_it.pdf"
pharma = "ind_nifty_pharma.pdf"
realty = "ind_nifty_realty.pdf"
con_dur = "Factsheet_nifty_consumer_durables.pdf"
oil_gas = "Factsheet_nifty_oil_and_gas.pdf"
energy = "ind_nifty_energy.pdf"
indices = ["auto","bank","fin_serv","fmcg","health","it","pharma","realty","con_dur","oil_gas","energy"]
option = ["[1] open indices","[2] open groww"]
while True:
    for j in option:
        print(j)

    cmd = input("--$ ")
    if cmd == "1":
        c = 0
        for i in indices:
            c += 1
            print("[",c,"]"," ",i)
        ans = input("> [choose option] ")
        if ans == "1":
            url = indice + auto
            search(url)   
        elif ans == "2":
            url = indice + bank
            search(url)        
        elif ans == "3":
            url = indice + fin_serv
            search(url) 
        elif ans == "4":
            url = indice + fmcg
            search(url)
        elif ans == "5":
            url = indice + health
            search(url)
        elif ans == "6":
            url = indice + it
            search(url)
        elif ans == "7":
            url = indice + pharma
            search(url)        
        elif ans == "8":
            url = indice + realty
            search(url)
        elif ans == "9":
            url = indice + con_dur
            search(url)
        elif ans == "10":
            url = indice + oil_gas
            search(url)
        elif ans == "11":
            url = indice + energy
            search(url)
        else:
            print("< [invalid input] >")
    if cmd == "2":
        url = "https://groww.in/stocks/user/explore"
        search(url)