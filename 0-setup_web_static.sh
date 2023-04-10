#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

static_string="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias  \/data\/web_static\/current\/;\n\t}"

# update environment and install nginx
sudo apt update
sudo apt install -y nginx
sudo ufw allow 'Nginx HTTP'

# create static content folders and create test webpage
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# create symbolic link to static folders
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of static content root folder to current user and group
sudo chown -R ubuntu:ubuntu /data/

# edit nginx configuration file in place
sudo sed -i "s/server_name _;/$static_string/" /etc/nginx/sites-available/default

# restart nginx server
sudo service nginx restart
