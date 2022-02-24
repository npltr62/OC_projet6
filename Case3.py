import fnct
import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
cmd1='sudo rm -rf /var/www/html/wordpress'
cmd2='sudo mysql -u root < wp_rm.sql'
fnct.run(cmd1)
fnct.run(cmd2)