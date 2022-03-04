"""Prints information about an FMI observation station to the screen.

Usage:
    ./stationinfo.py

Author:
    @npltr62 - 01.03.2022
"""
import logging #import librairie logging permettant de logger les étapes du script
from time import strftime
import fnct
fnct.run('mkdir -p logs')
datestr = strftime('[%d_%m_%Y_%T]')
datebis = strftime('%Y_%m_%d')
logfileinfo = f'./logs/{datebis}.log'
logformat = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename=logfileinfo, filemode='w', level=logging.INFO, format=logformat)
logging.info('start script')
def main():
    package= fnct.distrib()
    cmd1= f'sudo {package} update'
    cmd2= f'sudo {package} install python3-distro python3-yaml -y'
    fnct.run(cmd1)
    fnct.run(cmd2)
    print("""
        1.init wordpress
        2.backup and upload ftp server
        3.hardreset wordpress
        4.restore last backup
        5.run crontab
        """)
    choice= input("What would you like to do? ")
    if choice=="1":
        logging.info('***init wordpress***')
        print("\n Launch install")
        exec(open("Case1.py").read())
    elif choice=="2":
        logging.info('***backup and upload ftp server***')
        print("\n Launch backup")        
        exec(open("Case2.py").read())
    elif choice=="3":
        logging.info('***hardreset wordpress***')
        print("\n Launch reset")
        exec(open("Case3.py").read())                
    elif choice=="4":
        logging.info('***restore last backup***')
        print("\n Launch restore") 
        exec(open("Case4.py").read())       
    elif choice=="5":
        logging.info('***run crontab***')
        print("\n Launch cronjob")            
        exec(open("Case5.py").read())       
    else:
        print("\n Choose an option, try again!")

if __name__ == '__main__':
    main()