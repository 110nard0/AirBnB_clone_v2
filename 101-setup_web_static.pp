# Setup web servers for static deployment
exec { 'configure server':
  command  => 'sudo apt -y update;
  sudo apt -y install nginx;
  sudo ufw allow 'Nginx HTTP';
  sudo service nginx start;
  sudo mkdir -p /data/web_static/shared/;
  sudo mkdir -p /data/web_static/releases/test/;
  echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html > /dev/null;
  sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
  sudo chown -R ubuntu:ubuntu /data/;
  sudo sed -i "44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
