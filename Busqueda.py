import os
import time
from datetime import datetime
import win32api

# Buscar el archivo en el directorio especificado
def search_file_in_dir(dirname, filename, subdirs=None, extensions=None):
    # Si subdirs es None, buscar en todos los subdirectorios
    if subdirs is None:
        subdirs = []
    # Si extensions es None, buscar archivos con cualquier extensión
    if extensions is None:
        extensions = []
    # Convertir las extensiones a minúsculas
    extensions = [ext.lower() for ext in extensions]
    # Lista para almacenar los nombres de archivo ya encontrados
    found_files = []
    # Empezar cronometro
    start_time = time.time()
    for root, dirs, files in os.walk(dirname):
        print(f"Buscando en: {root}")
        # Verificar si el directorio actual está en la lista subdirs
        if root in subdirs:
            # Buscar el archivo en el directorio actual
            for file in files:
                filepath = os.path.join(root, file)
                # Verificar si el archivo ya ha sido encontrado
                if file.lower() in found_files:
                    continue
                # Verificar si la extensión del archivo está en la lista de extensiones
                if extensions and not any(file.lower().endswith(ext) for ext in extensions):
                    continue
                # Verificar si el archivo coincide con el nombre buscado
                if file.lower() == filename.lower():
                    print(f"Archivo encontrado en: {filepath}")
                    found_files.append(file.lower())
                    return filepath
        elif subdirs:
            # Si subdirs no está vacío, saltar al siguiente directorio
            continue
        else:
            # Si subdirs está vacío, buscar en todos los subdirectorios
            for file in files:
                filepath = os.path.join(root, file)
                # Verificar si el archivo ya ha sido encontrado
                if file.lower() in found_files:
                    continue
                # Verificar si la extensión del archivo está en la lista de extensiones
                if extensions and not any(file.lower().endswith(ext) for ext in extensions):
                    continue
                # Verificar si el archivo coincide con el nombre buscado
                if file.lower() == filename.lower():
                    print(f"Archivo encontrado en: {filepath}")
                    found_files.append(file.lower())
                    return filepath
    elapsed_time = time.time() - start_time
    print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")

# Buscar la cadena de texto en el directorio especificado
def search_text_in_dir(dirname, text, subdirs=None, author=None, start_date=None, end_date=None):
    # Si subdirs es None, buscar en todos los subdirectorios
    if subdirs is None:
        subdirs = []
    start_time = time.time()  # Tiempo inicial
    found_files = []
    for root, dirs, files in os.walk(dirname):
        print(f"Buscando en: {root}") # Imprime la ruta del directorio actual
        # Verificar si el directorio actual está en la lista subdirs
        if root in subdirs:
            # Si el directorio está en la lista, buscar en todos los archivos del directorio actual
            for file in files:
                filepath = os.path.join(root, file) 
                try:
                    with open(filepath, 'r', encoding='utf8') as f:
                        content = f.read()
                        if text in content:
                            # Obtener información del archivo
                            info = os.stat(filepath)
                            file_author = win32api.GetUserNameFromSid(win32api.GetFileSecurity(filepath, win32api.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner())
                            file_date = datetime.fromtimestamp(info.st_mtime)
                            # Aplicar filtros de autor y fecha
                            if (author is None or file_author == author) and \
                               (start_date is None or file_date >= start_date) and \
                               (end_date is None or file_date <= end_date):
                                print(f"Texto encontrado en: {filepath}")
                                found_files.append(filepath)
                except:
                    pass  # Ignorar archivos que no se pueden abrir
        elif subdirs:
            # Si subdirs no está vacío, saltar al siguiente directorio
            continue
        else:
            # Si subdirs está vacío, buscar en todos los subdirectorios
            for file in files:
                filepath = os.path.join(root, file) 
                try:
                    with open(filepath, 'r', encoding='utf8') as f:
                        content = f.read()
                        if text in content:
                            # Obtener información del archivo
                            info = os.stat(filepath)
                            file_author = win32api.GetUserNameFromSid(win32api.GetFileSecurity(filepath, win32api.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner())
                            file_date = datetime.fromtimestamp(info.st_mtime)
                            # Aplicar filtros de autor y fecha
                            if (author is None or file_author == author) and \
                               (start_date is None or file_date >= start_date) and \
                               (end_date is None or file_date <= end_date):
                                print(f"Texto encontrado en: {filepath}")
                                found_files.append(filepath)
                except:
                    pass  # Ignorar archivos que no se pueden abrir
    elapsed_time = time.time() - start_time
    print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")
    return found_files