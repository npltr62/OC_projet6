import os
import distro
def distrib(): #détermination de la distribution linux
    return distro.name()
def run(cmd):
    os.system(cmd)
