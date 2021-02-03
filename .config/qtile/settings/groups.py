# Archivo de configuracion de los grupos de trabajo

from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys

groups = [Group(i) for i in [" ", " ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Cambiar de workspace
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Enviar ventana a workspace
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])