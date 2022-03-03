"""
Description:
    1. Compress wordpress directory and sql dumpfile into archive
    2. Upload archive to remote server
Author:
    @npltr62 - 01.03.2022
"""
import fnct #call functions and variables
import logging #call logging module
from time import strftime #call time module
datestr = strftime('%Y_%m_%d') #get current date in specific format
package= fnct.distrib() #detect witch installing package should be used
cmd1= f'sudo {package} install lftp -y'
cmd2=f'mkdir -p ~/backup; cp -R /var/www/html/wordpress /home/{fnct.user}/backup/; sudo mysqldump -u root wordpress > /home/{fnct.user}/backup/{datestr}_dump.sql'
cmd3=f'sudo tar -cvf /home/{fnct.user}/{datestr}_backup.tar.gz ~/backup'
cmd4=f'lftp sftp://{fnct.user}:{fnct.pwd}@{fnct.host} -e "mkdir -f backup; put -O ~/backup /home/{fnct.user}/{datestr}_backup.tar.gz; quit"'
logging.info('install ltfp package')
print('install ltfp package')
fnct.run(cmd1) #install ltfp package
logging.info('dump wordpress database')
print('dump wordpress database')
fnct.run(cmd2) #dump wordpress database
logging.info('compress backup files')
print('compress backup files')
fnct.run(cmd3) #compress backup files
logging.info('start transfer to ftp server')
print('start transfer to ftp server')
fnct.run(cmd4)#upload archive to ftp server