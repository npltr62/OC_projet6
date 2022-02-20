#!/bin/bash
# special.sh
user= $1
pwd= $2
host= $3
datestr = $4
sudo mysqldump -u root wordpress > datestr_dump.sql
lftp sftp://user:pwd@host -e "mkdir -f backup; put -E -O ~/backup dump.sql; quit") | sort - | uniq - | crontab -