import paramiko
import ast
import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
# with open('C:\\Users/alouette\\Documents\\p6\\OC_projet6\\config.yaml') as f:
#     config = yaml.load(f, Loader=yaml.FullLoader)
# print(config['vms']['vm1']['user'])
# vm1_user = config['vms']['vm1']['user']
host='192.168.1.30'
user='np'
pwd='np'
def connection(host, user, pwd): #détermination de la distribution linux
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, username=user, password=pwd, port=22)
    stdin,stdout,stderr=ssh_client.exec_command('lsb_release -i')
    extract_distrib= ''.join(stdout.readlines()).split()[2]
    return extract_distrib
distrib=connection('192.168.1.25', 'np','np')
print(distrib)