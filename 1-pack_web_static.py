#!/usr/bin/python3
"""
script para generar un archivo .'tgz'
-	desde el contenido de web static del AirBnB Clone repo.
-	using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    function que devuelve el archivo
    sino devuelve None
    """
    local("mkdir -p versions/")
    time = datetime.now().strftime("%Y%M%d%H%M%S")
    name_file = "versions/web-static_{}.tgz".format(time)
    try:
        local("tar -cvzf {} web_static/".format(name_file))
        return name_file
    except Exception:
        return None
