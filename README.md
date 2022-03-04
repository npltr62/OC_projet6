# Projet 6 @Openclassroom @Administrateurinfrastructure&cloud

Il s'agit d'un script permettant d'automatiser les taches de la vie courante d'un site wordpress distant depuis un serveur ftp, à savoir :

1. l'installation
2. la sauvegarde
3. la restauration
4. la programmation d'une sauvegarde

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
|   3   |  hardreset wordpress    |    Supprime **totalement** le site wordpress: <ol><li> Suppression du répertoire wordpress </li><li> Drop de la base de donnée wordpress</li></ol>   |
|   4   | restore last backup    |    Importe le backup (configuré dans le yaml) et le réinjecte dans la base de donnée: <ol><li> Download de l'archive tar.gz</li><li> Décompression de l'archive et copie du répertoire wordpress</li><li>Restore de la base de donnée wordpress</li></ol>    |
|   5   |  run cronjob    |    Programme l'éxécution d'un shell ``backup_upload.sh`` à une heure/fréquence indiquée dans le fichier yaml ; <br> backup_upload.sh adopte le même comportement que le choix 2  |



## Fabriqué avec

_exemples :_
* [Python](https://www.python.org/) - Python
* [distro](https://github.com/python-distro/distro) - Module Python de détermination de l'OS et sa distribution
* [yaml](https://pyyaml.org/) - Module d'analyse et de génération de code YAML


## Auteur
* **Nicolas.P** _alias_ [@npltr62](https://github.com/npltr62)

