#!/bin/zsh

VIRTUAL_ENV=`poetry env info -p`

# * Delete remenants
echo "Deleting ./poetry.lock..."
rm -rf ./poetry.lock
echo "Deleting $VIRTUAL_ENV ..."
rm -rf $VIRTUAL_ENV

# * Reinstall dependencies
echo "Installing dependencies..."
poetry install