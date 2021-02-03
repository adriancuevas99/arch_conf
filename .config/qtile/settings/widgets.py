# Archivo de configuracion de los widget de la barra superior

from libqtile import widget
from settings.theme import color

widget_defaults = dict(
     font='JetBrainsMono Nerd Font',
     fontsize=17,
     padding=3,
    )
extension_defaults = widget_defaults.copy()

base = lambda fg='texto', bg='negro': {
    'foreground': color[fg],
    'background': color[bg]
}

flecha = lambda fg="blanco", bg="fondo": widget.TextBox(
    **base(fg,bg),
    text="", # nf-oct-triangle_left
    fontsize=37,
    padding=-4
)

principal = [
    # Grupos de trabajo
    widget.GroupBox(
        font='UbuntuMono Nerd Font',
        fontsize=23,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=color['activo'],
        inactive=color['inactivo'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=color['pop-up'],
        this_current_screen_border=color['marcado'],
        disable_drag=True
    ),
    # Nombre de la ventana
    widget.WindowName(
        foreground=color['ventana'],
        fontsize=21,
        font='UbuntuMono Nerd Font',
    ),
    flecha('color1', 'fondo'),
    widget.TextBox(
        background=color['color1'],
        foreground=color['blanco'],
        text=' '
    ),
    # Los accesos del sistema (WiFi, blueetooth,...)
    widget.Systray(
        fontsize=45,
        background=color['color1'],
    ),
    flecha('color2', 'color1'),
    widget.TextBox(
        background=color['color2'],
        foreground=color['fondo'],
        text=' '
    ),
    # Velocidad de la CPU i freqüencia
    widget.CPU(
        background=color['color2'],
        foreground=color['fondo'],
        format='CPU: {freq_current}GHz {load_percent}%',
    ),
    # Memoria RAM en uso
    widget.Memory(
        background=color['color2'],
        foreground=color['fondo'],
        format='MEM: {MemUsed}M',
    ),
    # Espacio disonible y porcentaje
    widget.DF(
        background=color['color2'],
        foreground=color['fondo'],
        partition='/',
        measure='G',
        format='SSD: {uf}{m} {r:.0f}%',
        visible_on_warn=False,
    ),
    flecha('color3', 'color2'),
    widget.TextBox(
        background=color['color3'],
        foreground=color['fondo'],
        text=' '
    ),
    # Reloj
    widget.Clock(
        background=color['color3'],
        foreground=color['fondo'],
        format='%d/%m/%y-%H:%M',
    )
]
