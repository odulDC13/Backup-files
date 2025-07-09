import os
import shutil

def copy_files(source_folder, destination_folder):
    # Verificar si la carpeta de destino existe, si no, crearla
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Recorrer todos los archivos y directorios en la carpeta de origen
    for root, dirs, files in os.walk(source_folder):
        # Construir la ruta de destino correspondiente a la carpeta actual
        destination_root = root.replace(source_folder, destination_folder, 1)

        # Verificar si la carpeta de destino existe, si no, crearla
        if not os.path.exists(destination_root):
            os.makedirs(destination_root)

        # Copiar todos los archivos en la carpeta actual a la carpeta de destino
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_root, file)
            shutil.copyfile(source_path, destination_path)

    print("Archivos copiados correctamente.")

# Carpeta de origen (Documentos del usuario actual)
source_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')

# Carpeta de destino (relativa a la ubicación del script)
script_dir = os.path.dirname(os.path.abspath(__file__))
destination_folder = os.path.join(script_dir, 'files')

# Llamar a la función para copiar los archivos
copy_files(source_folder, destination_folder)
