import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
syntaxe= config['cron']['syntaxe']
package= fnct.distrib()
cmd1= f'(crontab -l; echo "{syntaxe} mysqldump -u root wordpress > dump.sql",) | sort - | uniq - | crontab -'
cmd2=f'lftp sftp://{user}:{pwd}@{host} -e "get /backups/dump.sql; quit"'
cmd3='sudo mysql -u root < dump.sql'
fnct.run(cmd1)
logging.info('start download from ftp server')
fnct.run(cmd2)
logging.info('start dump')
fnct.run(cmd3)