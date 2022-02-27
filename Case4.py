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
cmd2=f'lftp sftp://{user}:{pwd}@{host} -e "get ~/backup/{datestr}_backup.tar.gz ; quit" && sudo tar -xf {datestr}_backup.tar.gz -C /var/www/html --strip-components=3'
cmd3=f'sudo mysql -u root wordpress < /var/www/html/{datestr}_dump.sql && sudo rm -f /var/www/html/{datestr}_dump.sql'
cmd4='sudo chown -R www-data:www-data /var/www/html/wordpress'
cmd5='sudo cp /wp_conf/wp-config.php /var/www/html/wordpress/'
fnct.run(cmd1)
logging.info('start download from ftp server')
print('start download from ftp server')
fnct.run(cmd2)
logging.info('start restore dump')
print(('start restore dump'))
fnct.run(cmd3)
logging.info('change right access')
print('change right access')
fnct.run(cmd4)
logging.info('copy worpress php config')
print('copy worpress php config')
fnct.run(cmd5)