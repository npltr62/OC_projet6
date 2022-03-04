"""
/***************************************************************************
    Wordpress_actions
    
    GitHub repo : https://github.com/npltr62/OC_projet6
                              -------------------
        Date                  : 01.03.2022
        Author                : @npltr62
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 * This program is usefull to automate some actions of your wordpress site *
 *               Initialize a Wordpress configuration                      *
 *               Backup a site and upload to remote server                 *
 *               Hard reset a Wordpress configuration                      *
 *               Download a backup from a remote server and restore it     *
 *               Schedule a backup job                                     *
 ***************************************************************************/
"""
import logging #import librairie logging permettant de logger les étapes du script
from time import strftime #call time module
import fnct #call functions
fnct.run('mkdir -p logs') #create logs folder
date = strftime('%Y_%m_%d') #create logs folder
logfileinfo = f'./logs/{date}.log' #logfile name
logformat = '%(asctime)s %(levelname)s %(message)s' #logformat
logging.basicConfig(filename=logfileinfo, filemode='w', level=logging.INFO, format=logformat) #log config
logging.info('start script')
def main():
    package= fnct.distrib() #detect witch installing package should be used
    cmd1= f'sudo {package} update' 
    cmd2= f'sudo {package} install python3-distro python3-yaml -y' 
    fnct.run(cmd1) #check updates
    fnct.run(cmd2) #install distro and yaml packages
    print("""
        1.init wordpress
        2.backup and upload ftp server
        3.hardreset wordpress
        4.restore last backup
        5.run cronjob
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