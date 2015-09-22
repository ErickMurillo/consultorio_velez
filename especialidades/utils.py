import os

def get_file_path(intance,filename):
    return os.path.join(intance.fileDir, filename)