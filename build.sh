#!/bin/sh
basedir=$(readlink -e $(dirname "$0"))
protodir="$basedir/proto/"


##
# Python protos

outdir="$basedir/_python-generated"
finaldir="$basedir/python/hsproto"

# Create directories
test -d "$outdir" && rm -rf "$outdir"
test -d "$finaldir" && rm -rf "$finaldir"
mkdir -p "$outdir"

# Generating python protobuf files
find "$protodir" -type f -name '*.proto' -exec protoc --proto_path="$protodir" --python_out="$outdir" {} \;

# Fix the generated protobuf files
find "$outdir" -name '*.py' -exec python3 "$basedir/python/relativize_module.py" "$outdir" {} \+

# Final move
mv "$outdir" "$finaldir"
