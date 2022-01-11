import yaml #import librairie yaml pour le fichier conf
import logging #import librairie logging permettant de logger les étapes du script
with open('C:\\Users/alouette\\Documents\\p6\\OC_projet6\\config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
print(config['vms']['vm1']['user'])
vm1_user = config['vms']['vm1']['user']
print("""
    1.install wordpress
    2.backup and send to ftp server
    3.reset wordpress
    4.restore last backup
    """)
choice= input("What would you like to do? ")
if choice=="1":
    print("\n Launch install")
elif choice=="2":
    print("\n Launch backup")
elif choice=="3":
    print("\n Launch reset")
elif choice=="4":
    print("\n Launch restore") 
else:
    print("\n Choose an option, try again!")