# Archivo de configuracion del las pantallas y barras

from libqtile.config import Screen
from libqtile import bar
from settings.widgets import principal
import subprocess

screens = [Screen(top=bar.Bar(principal, 24))]
