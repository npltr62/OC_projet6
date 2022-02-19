# Projet 6 @Openclassroom @Administrateurinfrastructure&cloud

Il s'agit d'un script permettant d'automatiser les taches de la vie courante d'un site wordpress distant depuis un serveur ftp, à savoir :

1. l'installation
2. la sauvegarde
3. la restauration

### Pré-requis
***Utiliser sudo sans mot de passe***
Au préalable, il s'agit d'avoir distinctement 2 serveurs
- un serveur FTP
- un serveur web avec WordPress basé indiferement sous Debian ou RedHat 

### Installation
Télécharger archive du projet avec ***curl***
`` curl -L https://github.com/npltr62/OC_projet6/archive/master.tar.gz | tar xz``

ou avec ***wget***
`` wget -c https://github.com/npltr62/OC_projet6/archive/master.tar.gz -O - | tar xz``

## Démarrage
Remplir le fichier de configuration config.yaml
le démarrage se déroule en ***local***
_exemple_: Executez la commande ``python3 script.py`` pour commencer ensuite [...]


``      1. install wordpress
        2. backup and upload to ftp server
        3. hardreset wordpress
        4. restore last backup
        5. run cronjob
``
|   Choix   |  Comportement    |
|---    |:-:    |
|   1   |   Permet d'initialiser un site wordpress :
        1. Télécharger les packets nécessaires
        2. Installer une base de donnée mariadb
        3. Lier la base de donnée sql à Wordpress   |
|   2   |    Execute un backup de la base de donnée nommée ***wordpress** et l'envoi sur le serveur configuré au préalable dans le fichier yaml  |
|   3  |   ROLLING ON THE FLOOR LAUGHING   |
|   4  |   GRINNING FACE   |
|   5  |   FACE WITH TEARS OF JOY  |



## Fabriqué avec

_exemples :_
* [Python](https://www.python.org/) - Python
* [distro](https://github.com/python-distro/distro) - Module Python de détermination de l'OS et sa distribution

## Auteur
* **Nicolas.P** _alias_ [@npltr62](https://github.com/npltr62)

