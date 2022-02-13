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
cmd1= f'sudo {package} update && {package} full-upgrade -y'
cmd2= f'sudo {package} install apache2 mariadb-server mariadb-client php libapache2-mod-php php-cli php-mysql php-zip php-curl php-xml wget -y'
cmd3='sudo mysql -u root < wp.sql'
cmd4='sudo wget -c https://wordpress.org/latest.tar.gz && sudo tar -xzf  latest.tar.gz -C /var/www/html'
cmd5='sudo rm /var/www/html/latest.tar.gz'
cmd6='sudo chown -R www-data:www-data /var/www/html/wordpress'
cmd7='sudo cp /wp_conf/wp-config.php /var/www/html/wordpress/ '
fnct.run(cmd1)
fnct.run(cmd2)
fnct.run(cmd3)
fnct.run(cmd4)
fnct.run(cmd5)
fnct.run(cmd6)
fnct.run(cmd7)