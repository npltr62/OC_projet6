import paramiko
import distrib
import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, username=user, password=pwd, port=22)
stdin,stdout,stderr=ssh_client.exec_command('apt-get purge wordpress')