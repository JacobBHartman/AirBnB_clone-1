#!/usr/bin/env bash
# Setup a server for the deployment of 'web_static' for AirBnB clone
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# create the directory and any parent folders as needed
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# create a fake file with simple content
sudo echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee -i /data/web_static/releases/test/index.html

# create another file that acts as a symbolic link to a directory
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# grant ownership permissions to user:'ubuntu' and group
sudo chown -R ubuntu:ubuntu /data/

# update the nginx configuration to serve the content of a folder
sudo sed -i "42i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\n" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
