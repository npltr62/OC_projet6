import fnct
import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
cmd1='sudo rm -rf /var/www/html/wordpress /var/www/html/'
cmd2='sudo mysql -u root < drop_wp.sql'
logging.info('remove worpress folder')
print('remove wordpress folder')
fnct.run(cmd1)
logging.info('drop wordpress database')
print('drop wordpress database')
fnct.run(cmd2)