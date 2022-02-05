import os
import paramiko
import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vms']['vm1']['user']
host= config['vms']['vm1']['host']
pwd= config['vms']['vm1']['pwd']
logging.info('start')
package= fnct.distrib(host,user,pwd)
cmd1= f'sudo {package} update && {package} full-upgrade -y'
cmd2= f'sudo {package} install apache2 mariadb-server mariadb-client php libapache2-mod-php php-cli php-mysql php-zip php-curl php-xml wget -y'
cmd3='sudo mysql -u root < wp.sql'
cmd4='sudo wget -c https://wordpress.org/latest.tar.gz && sudo tar -xzf  latest.tar.gz -C /var/www/html'
cmd5='sudo rm /var/www/html/latest.tar.gz'
cmd5='sudo chown -R www-data:www-data /var/www/html/wordpress'
cmd5='sudo cp /wp_conf/wp-config.php /var/www/html/wordpress/ '

# fnct.ssh(host,user,pwd, cmd1)
# fnct.ssh(host,user,pwd, cmd2)
# fnct.ssh(host,user,pwd, cmd3)
# fnct.upload_file(host, user, pwd,'C:\\Users/alouette\\Documents\\p6\\OC_projet6\\wp_conf\\wp.conf', '/etc/apache2/sites-available/wp.conf')
fnct.upload_file(host, user, pwd,'C:\\Users/alouette\\Documents\\p6\\OC_projet6\\wp_conf\\wp-config.php', f'/home/{user}/wp-config.php')
# fnct.upload_file(host, user, pwd,'C:\\Users/alouette\\Documents\\p6\\OC_projet6\\wp_conf\\wp.sql', f'/home/{user}/wp.sql')
# def install_function():
#     os.system('sudo apt-get update')

# install_function()