#!/usr/bin/python3
"""Creates and distributes an archive of static content to web servers"""
from fabric.api import env, local, put, run
from datetime import datetime
import os.path

env.hosts = ['52.204.195.22', '3.83.238.160']
env.user = 'ubuntu'


def do_pack():
    """Creates a tar.gz file with a custom name and saves it in a folder

    Returns:
        archive path (SUCCESS) or None (FAIL)
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    path_to_archive = "versions/web_static_" + now + ".tgz"

    local('mkdir -p versions')
    result = local('tar -cvzf {} web_static/'.format(path_to_archive))

    if result.succeeded:
        return path_to_archive
    return None


def do_deploy(archive_path):
    """Sends tar.gz archive folder to web servers and deploys an index page

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


def deploy():
    """Calls two functions and returns a boolean
    """
    return do_deploy(do_pack())
