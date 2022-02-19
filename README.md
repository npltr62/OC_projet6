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
Voici les options possibles:

|   Choix   |  Intitulé    |  Comportement    |
|-----------|--------------|------------------|
|   1   |  install wordpress    |    Permet d'initialiser un site wordpress :   <ol style={text-align: right;}><li>Télécharger les packets nécessaires</li><li>Installer une base de donnée</li><li>Lier la base de donnée sql à Wordpress</li></ol>    |
|   2   |  install wordpress    |    Execute un backup de la base de donnée nommée ***wordpress** et l'envoi sur le serveur configuré au préalable dans le fichier yaml   |
|   3   |  install wordpress    |    ROLLING ON THE FLOOR LAUGHING    |
|   4   |  install wordpress    |    GRINNING FACE    |
|   5   |  install wordpress    |    FACE WITH TEARS OF JOY   |



## Fabriqué avec

_exemples :_
* [Python](https://www.python.org/) - Python
* [distro](https://github.com/python-distro/distro) - Module Python de détermination de l'OS et sa distribution

## Auteur
* **Nicolas.P** _alias_ [@npltr62](https://github.com/npltr62)

