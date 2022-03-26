#!/bin/sh
#rotation.sh
#auteur: NP
#description: 
    #assurer la rotation des sauvegardes => supprime les archives de +7 jours
find . -type f -name '*.tar.gz' -mtime +7 -exec rm -f {} \;