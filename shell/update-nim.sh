#/bin/sh

# Update to the latest NIM compiler and tools

WORKDIR="$HOME/workspace/nim/compiler"
BINARY="./koch"

cd $WORKDIR
$BINARY boot -d:release
$BINARY nimble
$BINARY tools
cd
