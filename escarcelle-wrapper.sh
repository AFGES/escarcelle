#!/bin/sh
dir="${XDG_DATA_HOME:-$HOME/.local/share}/escarcelle"
bin="$dir/EscarcelleLinux"
mkdir -p "$dir"
if [ ! -f "$bin" ]; then
    cp /app/bin/EscarcelleLinux "$bin"
    chmod +x "$bin"
fi
exec "$bin" "$@"
