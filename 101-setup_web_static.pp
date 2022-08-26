# Automatizar la tarea 1

exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['nginx'],
}

exec {'nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['inicio web server'],
}

exec {'inicio web server':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['create_directory'],
}

exec {'create_directory':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['create_other_directory'],
}

exec {'create_other_directory':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['content_for_html'],
}

exec {'content_for_html':
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
  before   => Exec['create_symbolic_link'],
}

exec {'create_symbolic_link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['put_fabric'],
}

exec {'put_fabric':
  provider => shell,
  command  => 'sed -i "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default',
  before   => Exec['restart web server'],
}

exec {'restart web server':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['data file'],
}

file {'data file':
  ensure  => directory,
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}