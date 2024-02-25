#!/bin/bash
pyinstaller \
-F --name $1 --noconfirm \
--paths /api/src/ \
--distpath /api/bin \
main.py
