#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the
web_static folder in AirBnB Clone repository
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Creates a tar.gz file with a custom name and saves it in a folder

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
