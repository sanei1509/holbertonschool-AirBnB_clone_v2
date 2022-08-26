# Automatizar la tarea 1

#Update
exec { 'update'
  provider => shell,
  command => 'sudo apt-get -y update'
  before => Exec['nginx'],
}

#Instalar nginx
exec { 'nginx'
  provider => shell,
  command =>  command => 'sudo apt-get -y install nginx',
  before => Exec['crear carpetas'],
}

#Crear carpetas
exec { 'crear carpetas':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/; sudo mkdir -p /data/web_static/shared/',
  before   => Exec['creando contenido'],
}

#Añadiendo contenido estatico
exec { 'creando contenido':
  provider => shell,
  command  => 'echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
',
  before   => Exec[creo symbolic link],
}

#
#Creando link simbolico
exec { 'creo symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['create alias config'],
}

#Creando la configuración del alias para nuestra vista
exec { 'create alias config':
  provider => shell,
  command  => 'sed -i "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default',
  before   => Exec['restart web server'],
}

#Reiniciamos nginx para confirmar configuración
exec {'restart web server':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['data file'],
}

file {'data file'
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}