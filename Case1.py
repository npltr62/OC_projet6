"""
Description:
    1. Install all packages required for wordpress installation
    2. Create wordpress database
    3. Link database to wordpress 
Author:
    @npltr62 - 01.03.2022
"""
import fnct #call functions and variables
import logging #call logging module
package= fnct.distrib() #detect witch installing package should be used
cmd1= f'sudo {package} install apache2 mariadb-server mariadb-client php libapache2-mod-php php-cli php-mysql php-zip php-curl php-xml wget -y'
cmd2='sudo mysql -u root < wp_conf/wp.sql'
cmd3='sudo wget -c https://wordpress.org/latest.tar.gz && sudo tar -xzf latest.tar.gz -C /var/www/html && sudo rm /var/www/html/latest.tar.gz'
cmd4='sudo chown -R root:root /var/www/html/wordpress'
cmd5='sudo cp wp_conf/wp-config.php /var/www/html/wordpress/'
print('install all packages ')
fnct.run(cmd1) #install all packages required for wordpress installation
logging.info('create wordpress database')
print('create wordpress database')
fnct.run(cmd2) #run sql instructions in order to create wordpress database
logging.info('Download latest wordpress archive')
print('Download latest wordpress archive')
fnct.run(cmd3) #download latest wordpress and extract it in html folder
logging.info('change right access')
print('change right access')
fnct.run(cmd4) #change the owner of wordpress folder recursively
logging.info('copy worpress php config')
print('copy worpress php config')
fnct.run(cmd5) #copy php setting in wordpress folder
