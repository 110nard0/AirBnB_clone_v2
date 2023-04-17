#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the
web_static folder in AirBnB Clone repository
and distributes it to connected web servers
"""
from fabric.api import lcd, local, put, run, sudo
from datetime import datetime
from os import path


env.hosts = ['54.152.106.255', '100.25.181.181']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Sends tar.gz archive folder to web servers

    Returns:
        True (script works) or False (otherwise)
    """
    try:
        if not path.exists(archive_path):
            return False
        else:
            # upload archive
            put(archive_path, '/tmp/')

            # create target directory
            archive = archive_path[:-4]
            sudo('mkdir -p /data/web_static/releases/{}'.format(archive))
            
            # uncompress archive to target directory
            run('tar -xvzf /tmp/{} -C /data/web_static/releases/{}'.
                format(archive_path, archive))

            # delete archive
            run('rm /tmp/{}'.format(archive_path))

            # delete pre-existing symbolic link
            sudo('rm -rf /data/web_static/current')

            # create new symbolic link to archive content
            sudo('ln -sf /data/web_static/releases/{} 
                          /data/web_static/current'.format(archive))
    except:
        return False
    return True
