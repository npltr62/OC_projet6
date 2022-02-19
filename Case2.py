import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
from time import strftime
datestr = strftime('%d_%m_%Y_%T')
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
package= fnct.distrib()
cmd1= f'sudo {package} install lftp -y'
cmd2='mkdir -p ~/backup; sudo mysqldump -u root wordpress > /home/backup/dump.sql'
cmd3=f'lftp sftp://{user}:{pwd}@{host} -e "mkdir -f backup; put -O ~/backup /home/{user}/backup/dump.sql; quit"'
logging.info('install ltfp package')
fnct.run(cmd1)
logging.info('run dump wordpress database')
fnct.run(cmd2)
logging.info('start transfer to ftp server')
fnct.run(cmd3)