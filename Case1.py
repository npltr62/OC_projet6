"""Prints information about an FMI observation station to the screen.

Usage:
    ./stationinfo.py

Author:
    David Whipp - 26.9.2018
"""
import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user']
host= config['vm']['host']
pwd= config['vm']['pwd']
logging.info('start')
package= fnct.distrib()
cmd1= f'sudo {package} install apache2 mariadb-server mariadb-client php libapache2-mod-php php-cli php-mysql php-zip php-curl php-xml wget -y'
cmd2='sudo mysql -u root < wp_conf/wp.sql'
cmd3='sudo wget -c https://wordpress.org/latest.tar.gz && sudo tar -xzf latest.tar.gz -C /var/www/html && sudo rm /var/www/html/latest.tar.gz'
cmd4='sudo chown -R www-data:www-data /var/www/html/wordpress'
cmd5='sudo cp wp_conf/wp-config.php /var/www/html/wordpress/'
print('install all packages ')
fnct.run(cmd1)
logging.info('install wordpress database')
print('install wordpress database')
fnct.run(cmd2)
logging.info('Download latest wordpress archive')
print('Download latest wordpress archive')
fnct.run(cmd3)
logging.info('change right access')
print('change right access')
fnct.run(cmd4)
logging.info('copy worpress php config')
print('copy worpress php config')
fnct.run(cmd5)
