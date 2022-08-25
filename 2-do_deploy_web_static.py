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


def do_deploy(archive_path):
    """Fabric script distributes archive to web servers """
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            # Nombre del archivo CON la extension (.tgz)
            filename = archive_path.split("/")[1]
            # Nombre del archivo SIN la extension
            filename_no_ext = filename.split(".")[0]
            # Ruta completa hacia el archivo SIN extension
            path = "/data/web_static/releases/" + filename_no_ext + "/"

            # Create directory sino existe aun
            run("mkdir -p " + path)
            run("tar -xzf /tmp/" + filename + " -C " + path)
            run("mv " + path + "web_static/*" + " " + path)
            run("rm /tmp/{}".format(filename))
            run("rm -rf " + path + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + path + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception:
            return False
