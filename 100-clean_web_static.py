#!/usr/bin/python3
"""Deletes out-of-date web_static archives
"""
from fabric.api import env, cd, run
import os

env.hosts = ['54.152.106.255', '100.25.181.181']
env.user = 'ubuntu'


def do_clean(number=0):
    """Deletes all uncecessary web static releases locally and on web servers

    Args:
        number (int): number of most recent archive versions to retain
    """
    number = 1 if int(number) == 0 else int(number)

    with cd.local('./versions'):
        local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
              xargs -d '\n' rm".format(1 + number))
    with cd('/data/web_static/releases/'):
        run("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
