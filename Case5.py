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
cmd1= f'(crontab -l; echo " {syntaxe} sudo mysqldump -u root wordpress > dump.sql && lftp sftp://{user}:{pwd}@{host} -e "mkdir -E -f backup; put -O ~/backup /home/{user}/backup/{datestr}_dump.sql; quit") | sort - | uniq - | crontab -'
logging.info('start set cronjob')
fnct.run(cmd1)