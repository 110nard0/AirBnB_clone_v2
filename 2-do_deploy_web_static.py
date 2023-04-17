#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the
web_static folder in AirBnB Clone repository
and distributes it to connected web servers
"""
from fabric.api import env, put, run 
impost os.path


env.hosts = ['54.152.106.255', '100.25.181.181']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Sends tar.gz archive folder to web servers

    Args:
        archive_path(str): path to .tgz archive

    Returns:
        True (script works) or False (otherwise)
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        archive = archive_path.split('/')[-1]
        file_name = archive.split('.')[0]
        path_to_file = "/data/web_static/releases/{}/".format(file_name)
        symlink = "/data/web_static/current"

        # upload archive
        put(archive_path, "/tmp/")

        # create target directory
        run("sudo mkdir -p {}".format(path_to_file))

        # uncompress archive to target directory
        run("sudo tar -xzf /tmp/{} -C {}".format(archive, path_to_file))

        # delete archive
        run("sudo rm /tmp/{}".format(archive))

        # move web_static content into hosting directory
        run("sudo mv {}web_static/* {}".format(path_to_file, path_to_file))

        # remove web_static sub-directory
        run("sudo rm -rf {}web_static".format(path_to_file))

        # delete pre-existing symbolic link
        run("sudo rm -rf {}".format(symlink))

        # create new symbolic link to archive content
        run("sudo ln -s {} {}".format(path_to_file, symlink))
        return True
    except:
        return False
