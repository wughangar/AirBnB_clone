#!/usr/bin/python3
"""
creating a variable staorage and calling storage method on it
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
