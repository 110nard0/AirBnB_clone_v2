#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the
web_static folder in AirBnB Clone repository
and distributes it to connected web servers
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.152.106.255', '100.25.181.181']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Sends tar.gz archive folder to web servers

    Args:
        archive_path(str): path to .tgz archive

    Returns:
        True (script works) or False (otherwise)
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')

        # create target directory
        created_at = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
            releases/web_static_{}/'.format(created_at))

        # uncompress archive to target directory
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
            /data/web_static/releases/web_static_{}/'.
            format(created_at, created_at))

        # delete archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(created_at))

        # move web_static content into hosting directory
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/'.
            format(created_at, created_at))

        # remove web_static sub-directory
        run('sudo rm -rf /data/web_static/releases/\
            web_static_{}/web_static'.format(created_at))

        # delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # create new symbolic link to archive content
        run('sudo ln -s /data/web_static/releases/\
            web_static_{}/ /data/web_static/current'.format(created_at))
    except Exception as e:
        return False

    return True
