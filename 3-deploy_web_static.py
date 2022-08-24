#!/usr/bin/python3
"""
fabric script
-	que distribuya un archivo a nuestros servidores web
-	using the function do_deploy
"""
import os
from fabric.api import run, put, env

env.hosts = ['54.226.169.216', '54.91.221.19']
# env.user = "ubuntu"

def do_deploy(archive_path):
    """Fabric script distributes archive to web servers """
    if os.path.exists(archive_path) == False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            """ file_name name of file with .tgz """
            file_name = archive_path.split("/")[1]
            """ file_name2 name of file without .tgz """
            file_name2 = file_name.split(".")[0]
            """ final_name name of path of directory """
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
        except:
            return False