#!/usr/bin/python3
'''
    a Fabric script that generates a .tgz archive from the contents
    of the 'web_static' folder of your AirBnB Clone repo, using
    the function 'do_pack'
'''
from fabric.api import *
from time import strftime


def do_pack():
    archive_name = "web_static_" + strftime("%Y%m%d%H%M%S") + ".tgz"
    try:
        local("mkdir -p versions")
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None
