#!/bin/sh
SCRIPT="$(readlink -f $0)"
SCRIPTDIR=$(dirname "$SCRIPT")
cd "$SCRIPTDIR"

GENDIR="generated"
FINAL_DIR="python/hsproto"

# Create directories
test -d "$GENDIR" && rm -rf "$GENDIR"
test -d "$FINAL_DIR" && rm -rf "$FINAL_DIR"
mkdir "$GENDIR"

# Generating protobuf files
find proto -name '*.proto' -exec protoc -Iproto "--python_out=$GENDIR" {} \+

# Fixing protobuf files
find "$GENDIR" -name '*.py' -exec python3 python/relativize_module.py "$GENDIR" {} \+

# Final move
mv "$GENDIR" "$FINAL_DIR"
