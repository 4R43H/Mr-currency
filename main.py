#/bin/python3
"""
This My mini project for bezzar of crypto currencys
coder --> Eliot Elderson (EE)
Email --> N0000000!
Created in --> 27 Agu 2022
support time --> forever :)
Please Email:((((( --> coderpy@yahoo.com 

"""

import requests as req 
from bs4 import BeautifulSoup as bs
import sys


cr_list = [
    'bitcoin',
    'ethereum',
    'dogecoin',
    'shiba-inu',
    'xrp',
    'binance-coin',
    'cardano',
    'solana',
    'stellar',
    'chainlink',
    'uniswap',
    'polygon',
    'avalanche',
    'tron',
    'litecoin',
    'cosmos',
    'monero',
    'quant',
    'algorand',
    'flow',
    'vechain']

def cons():
    print("Welcome to Mr currncy app!")
    print("You can type list to see list!")
    print("You can type exit to exit of this app!")
    print("")
    for x in cr_list:
        print(x)
        
    while True:
        arz_avalie = input("Enter your crypto currency! : ")
        if arz_avalie == "list":
            print(cr_list)

        if arz_avalie == "exit":
            print("have good time!")
            print("good bye!")
            sys.exit()

        if arz_avalie in cr_list:
            r = req.get("https://www.coindesk.com/price/"+arz_avalie+"/")

            if r.status_code == 200:
                soup = bs(r.text, 'html.parser')
                val1 = soup.find("span", class_="typography__StyledTypography-owin6q-0 jvRAOp")
                print(val1.text)

            elif r.status_code == 404:
                print("Oops! Not found.")

        else:
            print("Sorry!!\n"+"We are not support this crypto currency!")

if __name__ == "__main__":
    cons()