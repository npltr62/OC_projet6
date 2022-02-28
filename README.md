# Projet 6 @Openclassroom @Administrateurinfrastructure&cloud

Il s'agit d'un script permettant d'automatiser les taches de la vie courante d'un site wordpress distant depuis un serveur ftp, à savoir :

1. l'installation
2. la sauvegarde
3. la restauration

### Pré-requis
***Utiliser sudo sans mot de passe***
Au préalable, il s'agit d'avoir distinctement 2 serveurs
- un serveur FTP
- un serveur web basé indiferement sous Debian ou RedHat
***Le serveur web***

### Installation
Télécharger archive du projet avec ***curl***
`` curl -L https://github.com/npltr62/OC_projet6/archive/master.tar.gz | tar xz``

ou avec ***wget***
`` wget -c https://github.com/npltr62/OC_projet6/archive/master.tar.gz -O - | tar xz``

## Démarrage
Remplir le fichier de configuration config.yaml
le démarrage se déroule en ***local*** et il est **IMPORTANT** de conserver l'intégrité du répertoire afin de garentir le bon déroulement du script.
_exemple_: Executez la commande ``np@np:~/OC_projet6 python3 script.py``.

Choix possibles :

|   Choix   |  Intitulé    |  Description    |
|-----------|--------------|------------------|
|   1   |  install wordpress    |    Permet d'initialiser un site wordpress :   <ol><li>Télécharger les packets nécessaires</li><li>Installer une base de donnée</li><li>Lier la base de donnée sql à Wordpress</li></ol>    |
|   2   |  backup and upload to ftp server    |    Backup du site wordpress et upload vers le serveur ftp: <ol><li> Création (si non présent) d'un répertoire backup dans le répertoire personnel</li><li> Copie du dossier wordpress dans le répertoire backup</li><li> Dump de la base de donnée wordpress dans répertoire backup</li><li> Mise en archive tar.gz du répertoire backup</li><li> Upload de l'archive tar.gz vers le serveur ftp</li></ol>   |
|   3   |  hardreset wordpress    |    Supprime **totalement** le site wordpress et le reinitialise pour une éventuelle restauration (cf option 4)    |
|   4   | restore last backup    |    Importe le dernier backup et le réinjecte dans la base de donnée     |
|   5   |  run cronjob    |    Cette commande exporte un fichier ``backup_upload.sh`` qui sera éxécuté à la fréquence indiquée dans le fichier yaml ; <br> backup_upload.sh adopte le même comportement que le choix 2  |



## Fabriqué avec

_exemples :_
* [Python](https://www.python.org/) - Python
* [distro](https://github.com/python-distro/distro) - Module Python de détermination de l'OS et sa distribution

## Auteur
* **Nicolas.P** _alias_ [@npltr62](https://github.com/npltr62)

