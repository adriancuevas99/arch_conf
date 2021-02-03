# Archivo de configuracion del los temas

from os import path
import subprocess
import json
from settings.path import qtile_path

archivo = path.join(qtile_path, "themes", "antonio.json")

# Abre el archivo y lo mete dentro de una variable
with open(archivo) as json_a:
    # Carga el archivo json para que tenga sus propiedades
    color = json.load(json_a)
