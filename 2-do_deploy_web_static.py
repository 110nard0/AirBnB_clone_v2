#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the
web_static folder in AirBnB Clone repository
and distributes it to connected web servers
"""
from fabric.api import env, put, sudo
from os import path


env.hosts = ['54.152.106.255', '100.25.181.181']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Sends tar.gz archive folder to web servers

    Args:
        archive_path(str): path to .tgz archive

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
            archive = archive_path[9:-4]
            sudo('mkdir -p /data/web_static/releases/{}/'.format(archive))

            # uncompress archive to target directory
            archive_path = archive_path[9:]
            sudo('tar -xvzf /tmp/{} -C /data/web_static/releases/{}/'.
                format(archive_path, archive))

            # delete archive
            sudo('rm /tmp/{}'.format(archive_path))

            # move web_static content into hosting directory
            sudo('mv /data/web_static/releases/{}/web_static/* \
                 /data/web_static/releases/{}/'.format(archive, archive))

            # remove web_static sub-directory
            sudo('rm -rf /data/web_static/releases/{}/web_static'
                    .format(archive))

            # delete pre-existing symbolic link
            sudo('rm -rf /data/web_static/current')

            # create new symbolic link to archive content
            sudo('ln -sf /data/web_static/releases/{}\
                          /data/web_static/current'.format(archive))
    except Exception as e:
        return False

    return True
