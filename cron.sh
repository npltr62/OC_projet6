#!/bin/bash
mkdir -p ~/backup; cp -R /var/www/html/wordpress /home/$1/backup/; sudo mysqldump -u root wordpress > $4_dump.sql && lftp sftp://$1:$2@$3 -e "mkdir -f backup; put -E -O ~/backup $4_dump.sql; quit") | sort - | uniq - | crontab - && rm $4_dump.sql;
sudo tar -cvf /home/$1/$4_backup.tar.gz ~/backup;