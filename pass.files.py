import os
import shutil
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def copy_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        destination_root = root.replace(source_folder, destination_folder, 1)
        if not os.path.exists(destination_root):
            os.makedirs(destination_root)
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_root, file)
            shutil.copyfile(source_path, destination_path)

    print("Archivos copiados correctamente.")

source_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')
script_dir = get_base_path()
destination_folder = os.path.join(script_dir, 'files')

copy_files(source_folder, destination_folder)
