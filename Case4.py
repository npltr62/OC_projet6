"""Prints information about an FMI observation station to the screen.

Description:
    1. Download archive choosed from remote server
    2. Restore the wordpress database
    3. Link database to wordpress 

Author:
    @npltr62 - 01.03.2022
"""
import fnct #call functions
import env #call variables
import logging #call logging module
package= fnct.distrib() #detect witch installing package should be used
cmd1= f'sudo {package} install lftp -y'
cmd2=f'lftp sftp://{env.user}:{env.pwd}@{env.host} -e "get ~/backup/{env.datestr}_backup.tar.gz ; quit" && sudo tar -xf {env.datestr}_backup.tar.gz -C /var/www/html --strip-components=3'
cmd3=f'sudo mysql -u root wordpress < /var/www/html/{env.datestr}_dump.sql && sudo rm -f /var/www/html/{env.datestr}_dump.sql'
cmd4='sudo chown -R root:root /var/www/html/wordpress'
fnct.run(cmd1) #install ltfp package
logging.info(f'start download {env.datestr}_backup.tar.gz from ftp server')
print(f'start download {env.datestr}_backup.tar.gz from ftp server')
fnct.run(cmd2) #download archive from ftp server and extract it in html directory
logging.info('start restore dump')
print(('start restore dump'))
fnct.run(cmd3) #run sql instructions in order to restore wordpress database
logging.info('change right access')
print('change right access')
fnct.run(cmd4) #change the owner of wordpress folder recursively