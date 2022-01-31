#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""

from fabric.api import run
from fabric.api import local
from fabric.api import get
from fabric.api import put
from datetime import datetime
import os


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
