import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
from time import strftime
import fnct
fnct.run('mkdir logs')
datestr = strftime('[%d_%m_%Y_%T]')
datebis = strftime('%Y_%m_%d')
logfileinfo = f'./logs/{datebis}.log'
logformat = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename=logfileinfo, filemode='w', level=logging.INFO, format=logformat)
logging.info('Début du script')
def main():
    package= fnct.distrib()
    cmd1= f'sudo {package} update && {package} full-upgrade -y'
    cmd2= f'sudo {package} install python3-distro python3-yaml -y'
    fnct.run(cmd1)
    fnct.run(cmd2)
    print("""
        1.init wordpress
        2.backup and download ftp server
        3.hardreset wordpress
        4.restore last backup
        5.run crontab
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