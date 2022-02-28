"""Prints information about an FMI observation station to the screen.

Usage:
    ./stationinfo.py

Author:
    David Whipp - 26.9.2018
"""
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
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        logging.error(e)
