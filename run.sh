#!/bin/bash
set -e

for bot in $(cat config.json | jq -r 'to_entries[] | "\(.key),\(.value.source),\(.value.branch)"'); do
  name=$(echo $bot | cut -d',' -f1)
  source=$(echo $bot | cut -d',' -f2)
  branch=$(echo $bot | cut -d',' -f3)

  echo "Cloning $name from $source (branch: $branch)..."
  git clone --branch "$branch" --single-branch "$source" "$name"

  cd "$name"
  if [ -f requirements.txt ]; then
    pip install --no-cache-dir -r requirements.txt
  fi
  cd ..
done
