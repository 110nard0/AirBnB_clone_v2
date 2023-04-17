#!/usr/bin/python3
"""Deletes out-of-date web_static archives
"""
import os
from fabric.api import env, cd, lcd, run

env.hosts = ['54.152.106.255', '100.25.181.181']
env.user = 'ubuntu'


def do_clean(number=0):
    """Deletes all uncecessary web static releases locally and on web servers

    Args:
        number (int): number of most recent archive versions to retain
    """
    number = 1 if int(number) == 0 else int(number)

    versions = sorted(os.listdir('versions'))
    [versions.pop() for num in range(number)]

    with lcd('versions'):
        [local("rm ./{}".format(a)) for v in versions]

    with cd('/data/web_static/releases'):
        versions = run('ls -ltr').split()
        versions = [ver for ver in versions if "web_static_" in ver]
        [versions.pop() for x in range(number)]
        [run("rm -rf ./{}".format(v)) for v in versions]


#    with cd.local('./versions'):
#        local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
#              xargs -d '\n' rm".format(1 + number))
#    with cd('/data/web_static/releases/'):
#        run("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
#            xargs -d '\n' rm".format(1 + number))
