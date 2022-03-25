#!/bin/bash
#backup_upload.sh
#auteur: NP
#description: 
    # 1. Création (si non présent) d'un répertoire backup dans le répertoire personnel
    # 2. Copie du dossier wordpress dans le répertoire backup
    # 3. Dump de la base de donnée wordpress dans répertoire backup
    # 4. Mise en archive tar.gz du répertoire backup
    # 5. Upload de l'archive tar.gz vers le serveur ftp
mkdir -p ~/backup; cp -R /var/www/html/wordpress /home/$1/backup/; sudo mysqldump -u root wordpress > /home/$1/backup/$4_dump.sql && sudo tar -cvf /home/$1/$4_backup.tar.gz ~/backup && lftp sftp://$1:$2@$3 -e "mkdir -f backup; find ~/backup/* -type f -mmin +2 -exec rm  '{}';put -E -O ~/backup /home/$1/$4_backup.tar.gz; quit";