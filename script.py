import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
from time import strftime
datestr = strftime('[%d_%m_%Y_%T]')
datebis = strftime('%Y_%m_%d')
logfileinfo = f'./logs/{datebis}.log'
logformat = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename=logfileinfo, filemode='w', level=logging.INFO, format=logformat, encoding='utf-8')
def main():
    datestr = strftime('[%d_%m_%Y_%T]')
    datebis = strftime('%Y_%m_%d')
    logfileinfo = f'./logs/{datebis}.log'
    logformat = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(filename=logfileinfo, filemode='w', level=logging.INFO, format=logformat)
    logging.info('Début du script')
    print("""
        1.install LAMP server & wordpress
        2.backup and download ftp server
        3.hardreset wordpress
        4.restore last backup
        """)
    choice= input("What would you like to do? ")
    if choice=="1":
        logging.error('choix1')
        exec(open("Case1.py").read())
        print("\n Launch install")
    elif choice=="2":
        logging.info('choix2')
        exec(open("Case2.py").read())
        print("\n Launch backup")
    elif choice=="3":
        logging.info('choix3')
        exec(open("Case3.py").read())        
        print("\n Launch reset")
    elif choice=="4":
        logging.info('choix4')
        exec(open("Case4.py").read())       
        print("\n Launch restore") 
    else:
        print("\n Choose an option, try again!")

if __name__ == '__main__':
    main()