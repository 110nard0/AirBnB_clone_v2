#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

# update environment and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo apt install -y nginx
sudo ufw allow 'Nginx HTTP'
sudo service nginx start

# create static content folders and create test webpage
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# create symbolic link to static folders
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of static content root folder to current user and group
sudo chown -R ubuntu:ubuntu /data/

# edit nginx configuration file in place
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# restart nginx server
sudo service nginx restart
