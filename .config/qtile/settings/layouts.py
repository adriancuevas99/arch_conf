# Archivo de configuracion de los layouts

from libqtile import layout

layout_conf = {
    'border_focus': '#FFFFFF',
    'border_width': 1,
    'margin': 4
}

layouts = [
    # Pantalla completa
    layout.Max(**layout_conf),
    # Vertical en columnas
    #layout.Stack(num_stacks=3),
    # En vertical, cada pantalla ocupa mas espacio, las anteriores se van haciendo estrechas
    #layout.Bsp(),
    # Igual que MonadTall pero con menos opciones
    #layout.Columns(),
    # Todas las ventanas con los mismos tamaños tanto en vertical como horizontal
    #layout.Matrix(),
    # Ventana principal a la izquierda (se puede cambiar) se van generando al lado
    layout.MonadTall(**layout_conf),
    # Igual que MonadTall pero en vertical
    #layout.MonadWide(),
    # Depende de la cantidad de las ventanas va cambiano el formato
    #layout.RatioTile(),
    # Como MonadTall pero la ventana principal tiene mayor tamaño
    layout.Tile(**layout_conf),
    # Cuando no esta en Max, muestra en el lateral un con el orden las ventanas
    #layout.TreeTab(),
    # Lo ordena de forma horizontal sin prioridad de ventana
    #layout.VerticalTile(),
    # La ventana principal muy grande y las otras en un lateral el pequeño
    #layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], border_focus='#FFFFFF')