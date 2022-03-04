"""
Description:
    Schedule a backup to remote server

Author:
    @npltr62 - 01.03.2022
"""
import fnct #call functions
import env #call variables
import logging #call logging module
from time import strftime #call time module
package= fnct.distrib() #detect witch installing package should be used
datestr = strftime('%Y_%m_%d') #get current date in specific format
package= fnct.distrib() #detect witch installing package should be used
cmd1= f'sudo {package} install lftp -y; mkdir -p ~/.cron; cp backup_upload.sh ~/.cron/ && (crontab -l; echo "{env.syntaxe} sh /home/{env.user}/.cron/backup_upload.sh {env.user} {env.pwd} {env.host} {datestr}") | sort - | uniq - | crontab -'
logging.info('start set cronjob')
print(f'Set cronjob: {env.syntaxe}')
fnct.run(cmd1) #set cronjob in crontab