"""
Description:
    Python script which wrapping all functions and variables required

Author:
    @npltr62 - 01.03.2022
"""
import subprocess #import subprocess module
import distro #import distro module
import logging #import logging module
import yaml #call yaml module
with open('config.yaml') as f: #parsing yaml config file
    config = yaml.load(f, Loader=yaml.FullLoader)
user= config['vm']['user'] #get value from 'user' key
host= config['vm']['host'] #get value from 'host' key
pwd= config['vm']['pwd'] #get value from 'pwd' key
datestr = config['latest_dump_file']['date'] #get value from 'date' key
syntaxe= config['cron']['syntaxe'] #get value from 'syntaxe' key
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
