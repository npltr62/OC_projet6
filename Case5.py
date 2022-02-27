import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
from time import strftime
datestr = strftime('%Y_%m_%d')
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
syntaxe= config['cron']['syntaxe']
package= fnct.distrib()
cmd1= f'sudo {package} install lftp -y; mkdir -p ~/.cron; cp backup_upload.sh ~/.cron && (crontab -l; echo "{syntaxe} chmod +x /home/{user}/.cron/backup_upload.sh {user} {pwd} {host} {datestr}") | sort - | uniq - | crontab -'
logging.info('start set cronjob')
print('start set cronjob')
fnct.run(cmd1)