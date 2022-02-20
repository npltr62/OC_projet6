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
cmd1= f'mkdir /home/{user}/.cron; cp cron.sh /home/{user}/.cron && (crontab -l; echo "{syntaxe} chmod +x /home/{user}/.cron/cron.sh {user} {pwd} {host} {datestr}") | sort - | uniq - | crontab -'
logging.info('start set cronjob')
fnct.run(cmd1)