import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
package= fnct.distrib()
cmd1= f'sudo {package} install lftp -y'
cmd1='sudo mysqldump -u root wordpress> dump.sql'
cmd2=f'lftp sftp://{user}:{pwd}@{host} -e "put ~/dump.sql; quit"'
logging.info('start dump')
fnct.run(cmd1)
logging.info('start transfer to ftp server')
fnct.run(cmd2)