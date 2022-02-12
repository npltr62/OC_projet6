import fnct
import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
cmd1='sudo rm /var/www/html/wordpress'
cmd2='sudo mysql -u root < wp_rm.sql'
cmd3='sudo wget -c https://wordpress.org/latest.tar.gz && sudo tar -xzf  latest.tar.gz -C /var/www/html'
fnct.run(cmd1)
fnct.run(cmd2)
fnct.run(cmd3)