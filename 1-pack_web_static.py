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
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web-static_" + time
    try:
        local("tar -cvzf " + name + ".tgz web_static")
        return "{}.tgz".format(name)
    except:
        return None
