#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

db_value = os.getenv("HBNB_TYPE_STORAGE")
if db_value == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
