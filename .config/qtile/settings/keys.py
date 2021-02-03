# Archivo de configuracion de las keys

from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [
    # SISTEMA
    # Ventana anterior
    Key([mod], "k", lazy.layout.down()),
    # Ventana siguiente
    Key([mod], "j", lazy.layout.up()),
    # Cambio orden ventanas anterior
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    # Cambio orden ventanas siguiente
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),
    # Siguiente layout
    Key([mod], "Tab", lazy.next_layout()),
    # Cerrar ventana actual
    Key([mod], "w", lazy.window.kill()),
    # Reiniciar Qtile
    Key([mod, "control"], "r", lazy.restart()),
    # Cerrar sesión
    Key([mod, "control"], "q", lazy.shutdown()),
    # Pantalla completa
    Key([mod], "space", lazy.window.toggle_fullscreen()),

    # APPS
    # Buscar aplicacion
    Key([mod], "m", lazy.spawn("rofi -show drun -show-icons")),
    # Aplicaciones abiertas
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),
    # Firefox
    Key([mod], "f", lazy.spawn("firefox")),
    # VS Code
    Key([mod], "c", lazy.spawn("code")),
    # Alacritty
    Key([mod], "Return", lazy.spawn("alacritty")),
    # Captura de pantalla
    Key([mod], "s", lazy.spawn("scrot")),
    # Explorador de ficheros
    Key([mod], "t", lazy.spawn("thunar")),

    # GESTION DE DISPOSITIVOS
    # Bajar volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    # Subir volumen
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    # Silenciar
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    # Subir brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    # Bajar brillo
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]