#!/usr/bin/python3
"""
method initialize for the proyect
"""


from models.engine.file_storage import FileStorage
import models


storage = FileStorage()
storage.reload()
