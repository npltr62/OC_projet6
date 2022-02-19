import subprocess
import distro
import logging #import librairie logging permettant de logger les étapes du script
def distrib(): #détermination de la distribution linux
    yum = ['fedora', 'centos','redhat']
    if distro.id() in yum:
        return 'yum'
    else: 
        return 'apt'
def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, timeout=10, capture_output=True)
    except subprocess.CalledProcessError as e:
        logging.error(e)
