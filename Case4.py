import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
from time import strftime
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
datestr = config['latest_dump_file']['date']
package= fnct.distrib()
cmd1= f'sudo {package} install lftp -y'
cmd2=f'lftp sftp://{user}:{pwd}@{host} -e "get ~/backup/{datestr}_backup.tar.gz; quit" && sudo tar -xzf  {datestr}_backup.tar.gz -C /var/www/html'
cmd3='sudo mysql -u root wordpress < /var/www/html/wordpress/{datestr}_dump.sql'
fnct.run(cmd1)
logging.info('start download from ftp server')
fnct.run(cmd2)
logging.info('start restore dump')
fnct.run(cmd3)