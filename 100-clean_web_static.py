#!/usr/bin/python3
"""
fabric script
-	que borre los archivos obsoletos
-	using the function do_clean()
"""
import os
from fabric.api import run, put, env, local
from datetime import datetime

env.hosts = ['54.226.169.216', '54.91.221.19']
env.user = "ubuntu"


def do_clean(number=0):
    """despreciar(eliminar) las versiones obsoletas quedarnos con
    las actuales"""
    num = int(number)
    # ruta donde se encuentran almacenadas las versiones
    path = "/data/web_static/releases"
    # numero de elementos a borrar
    trash = num + 1
    if num == 0 or num == 1:
        local("cd versions; ls -t | tail -n +2 | xargs rm -rf")
        run("cd ; {}; ls -t | tail -n +2 | xargs rm -rf")
    else:
        local("cd versions; ls -t | tail -n +{} | xargs rm -rf".format(trash))
        run("cd {}; ls -t | tail -n +{} | xargs rm -rf".format(path, borrar))
