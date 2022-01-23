import paramiko
import fnct
import logging
import yaml #import librairie yaml pour le fichier conf
with open('C:\\Users/alouette\\Documents\\p6\\OC_projet6\\config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vms']['vm1']['user']
host= config['vms']['vm1']['host']
pwd= config['vms']['vm1']['pwd']
logging.info('start')
package= fnct.distrib(host,user,pwd)
cmd1= f'{package} update'
cmd2= f'{package} install -y wget apache2 php php-pdo php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath mariadb-server wordpress'
fnct.ssh(host,user,pwd, cmd1)
fnct.ssh(host,user,pwd, cmd2)
fnct.upload_file(host, user, pwd,'C:\\Users/alouette\\Documents\\p6\\OC_projet6\\\wp_conf\wp.conf', '/etc/apache2/sites-available/wp.conf')
fnct.upload_file(host, user, pwd,'C:\\Users/alouette\\Documents\\p6\\OC_projet6\\\wp_conf\config-myblog.example.com.php', '/etc/apache2/sites-available/wp.conf')