#!/usr/bin/python3
"""
fabric script
-	que distribuya un archivo a nuestros servidores web
-	using the function do_deploy
"""
import os
from fabric.api import run, put, env

env.hosts = ['54.226.169.216', '54.91.221.19']
env.user = "ubuntu"


def do_pack():
    """
    function que devuelve el archivo
    sino devuelve None
    """
    local("mkdir -p versions/")
    time = datetime.now().strftime("%Y%M%d%H%M%S")
    name_file = "versions/web_static_{}.tgz".format(time)
    try:
        local("tar -cvzf {} web_static/".format(name_file))
        return name_file
    except Exception:
        return None


def do_deploy(archive_path):
    """Fabric script distributes archive to web servers """
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            """ nombre del archivo con .tgz """
            file_name = archive_path.split("/")[1]
            """ nombre del archivo sin .tgz """
            file_name2 = file_name.split(".")[0]
            """ ruta completa hacia el archivo """
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception:
            return False


def deploy():
    """funcion para ejecutar la función completa"""
    path = do_pack()
    if os.path.exists(path):
        return do_deploy(path)
    else:
        return False
