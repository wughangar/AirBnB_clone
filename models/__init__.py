from engine.file_storage import FileStorage

file_path = "path/to/file"
objects = {}

storage = FileStorage(file_path, objects)

storage.reload()
