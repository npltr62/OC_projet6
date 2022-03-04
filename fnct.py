"""
Description:
    Python script which wrapping all functions and variables required

Author:
    @npltr62 - 01.03.2022
"""
import subprocess #import subprocess module
import distro #import distro module
import logging #import logging module
def distrib(): #check witch linux distribution is used and return the packaging name
    yum = ['fedora', 'centos','redhat']
    if distro.id() in yum:
        return 'yum'
    else: 
        return 'apt'
def run(cmd): #run subprocess command
    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        logging.error(e)
