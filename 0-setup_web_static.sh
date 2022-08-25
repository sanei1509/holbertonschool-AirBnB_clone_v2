#!/usr/bin/env bash
# Script que usen los servidores web creados para el deploy web static
# -f del ln -> si existe debe eliminarse y volver a crearse
sudo apt-get -y install nginx
sudo apt-get update
sudo apt-get -y upgrade

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current 
chown -R ubuntu:ubuntu /data/
sed -i "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
