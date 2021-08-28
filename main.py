import os
from pathlib import Path 
import sys
from typing import *
import ipaddress

class sitesControl:

    FILE_PATH = Path('C:\Windows\System32\drivers\etc')

    def __init__(self) -> None:
        self.path = self.FILE_PATH
        self.websites =  websites = []
        self.size = None
        self.ip = ipaddress.ip_address('127.0.0.1')
    
    def checkos(self) -> None:
        if not sys.platform.startswith('win'):
            raise SystemExit("Only Windows Is Supported!")
    
    def changePath(self) -> None:
        os.chdir(self.path)
    
    def changePerms(self) -> None:
        os.chmod("hosts", 0o777)

    def getinp(self) -> None:
        while True:
            try:
                self.size = int(input('Enter Number Of Sites To block: '))
                break
            except:
                print("invalid input please enter a number")
        
        for _ in range(self.size):
            website = input("Enter Wbsites: ").replace(" ", "").rstrip("/")
            self.websites.append(website)

    
    def addingList(self) -> None:
        with open('hosts', 'a') as f:
            for _ in range(self.size):
                for i in self.websites:
                    f.write("\n{}  {}".format(self.ip, i))
    
    def verification(self) -> None:
        for i in self.websites:
            print("Wesbsite {} Has Been Blocked. Please Refresh Your Browser.".format(i))



def main() -> None:
    control = sitesControl()
    control.checkos()
    control.changePath()
    control.changePerms()
    control.getinp()
    control.addingList()
    control.verification()

if __name__ == '__main__':
    main()

