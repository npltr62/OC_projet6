import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
from time import strftime
datestr = strftime('[%d_%m_%Y_%T]')
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
package= fnct.distrib()
cmd1= f'sudo {package} install lftp -y'
cmd2=f'sudo lftp sftp://{user}:{pwd}@{host} -e "get {datestr}_dump.sql; quit"'
cmd3='sudo mysql -u root < dump.sql'
fnct.run(cmd1)
logging.info('start download from ftp server')
fnct.run(cmd2)
logging.info('start dump')
fnct.run(cmd3)