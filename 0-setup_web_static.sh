#!/usr/bin/env bash
'''
sets up web servers for the deployment of web_static
'''

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
chmod -R ug+rwx /data/

