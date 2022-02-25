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
package= fnct.distrib()
cmd1= f'sudo {package} install lftp -y'
cmd2=f'mkdir -p ~/backup; cp -R /var/www/html/wordpress /home/{user}/backup/; sudo mysqldump -u root wordpress > /home/{user}/backup/{datestr}_dump.sql'
cmd3=f'sudo tar -cvf /home/{user}/{datestr}_backup.tar.gz ~/backup'
cmd4=f'lftp sftp://{user}:{pwd}@{host} -e "mkdir -f backup; put -O ~/backup /home/{user}/{datestr}_backup.tar.gz; quit"'
logging.info('install ltfp package')
print('install ltfp package')
fnct.run(cmd1)
logging.info('run dump wordpress database')
print('run dump wordpress database')
fnct.run(cmd2)
logging.info('tar dump files')
print('tar dump files')
fnct.run(cmd3)
logging.info('start transfer to ftp server')
print('start transfer to ftp server')
fnct.run(cmd4)