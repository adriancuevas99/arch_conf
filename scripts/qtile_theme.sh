#!/bin/bash

echo "Hora de cambiar el tema"

ccat ~/.config/qtile/settings/theme.py

echo "Que tema quieres cambiar"
read original
original="$original.json"

echo "Por cual tema quieres cambiarlo"

exa ~/.config/qtile/themes/

read nuevo
nuevo="$nuevo.json"

sed -i "s/$original/$nuevo/g" ~/.config/qtile/settings/theme.py


