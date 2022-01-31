#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""


from fabric.api import run
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import env
from datetime import datetime
import os

env.hosts = ['34.74.161.43', '35.185.60.222']


def do_pack():
    """ do_pack """
    complete_time = datetime.now()
    string_time = complete_time.strftime("%Y%m%d%H%M%S")
    tgz_name = string_time + '.tgz'
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{} web_static".format(tgz_name))
    path_tgz = 'versions/web_static_{}'.format(tgz_name)
    if os.path.exists(path_tgz):
        return path_tgz
    else:
        return None


def do_deploy(archive_path):
    """ do_deploy """
    if os.path.exists(archive_path):
        try:
            file_n = archive_path.split("/")[-1]
            no_ext = file_n.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(path, no_ext))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
            run('rm /tmp/{}'.format(file_n))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
            run('rm -rf {}{}/web_static'.format(path, no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
            return True
        except Exception:
            return False
    else:
        return False
