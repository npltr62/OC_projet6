"""Prints information about an FMI observation station to the screen.
Description:
    1. Remove wordpress folder
    2. Drop wordpress database

Author:
    @npltr62 - 01.03.2022
"""
import fnct #call functions and variables
import logging #call logging module
cmd1='sudo rm -rf /var/www/html/'
cmd2='sudo mysql -u root < wp_conf/drop_wp.sql'
logging.info('remove html folder')
print('remove html folder')
fnct.run(cmd1) #remove html folder
logging.info('drop wordpress database')
print('drop wordpress database')
fnct.run(cmd2) #run sql instructions in order to drop wordpress database