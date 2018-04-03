#!/usr/bin/python3
'''
    a Fabric script that generates a .tgz archive from the contents
    of the 'web_static' folder of your AirBnB Clone repo, using
    the function 'do_pack'
'''
from fabric.api import *
import os.path
from pathlib import Path
import os

env.hosts = ['54.157.250.230', '107.20.129.42']
env.user = 'ubuntu'

def do_deploy(archive_path):
    my_file = str(Path(archive_path))
    if os.path.isfile(my_file):
        archive_name = archive_path.split('/')[-1]
        put(local_path=archive_path, remote_path='/tmp/{}'.format(archive_name))
        file_wo_ext = archive_name.strip('.tgz')
        run("mkdir -p /data/web_static/releases/{}/".format(file_wo_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_name, file_wo_ext))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(file_wo_ext, file_wo_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_wo_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(file_wo_ext))
        return True
    else:
        return False
