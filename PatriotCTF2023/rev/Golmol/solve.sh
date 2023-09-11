#!/bin/bash

fl="./ok"

for i in {0..255}; do
    data="$i"
    result=$(echo -n "$data" | wine "$fl")
    if echo "$result" | grep -q "PCTF"; then
        echo "Int: $data"
        echo "Flag: $result"
        break
    else
        echo "Int: $data"
        echo "Flag: $result"
    fi
done
