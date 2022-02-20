#!/bin/bash
# special.sh
sudo mysqldump -u root wordpress > $4_dump.sql && lftp sftp://$1:$2@$3 -e "mkdir -f backup; put -E -O ~/backup $4_dump.sql; quit") | sort - | uniq - | crontab - && rm $4_dump.sql