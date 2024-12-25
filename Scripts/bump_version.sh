#!/bin/bash

# Check if version type is provided
if [ -z "$1" ]; then
    echo "Usage: $0 [major|minor|patch]"
    exit 1
fi

# Check for untracked files
UNTRACKED=$(git ls-files --others --exclude-standard)
if [ ! -z "$UNTRACKED" ]; then
    echo "Found untracked files:"
    echo "$UNTRACKED"
    read -p "Would you like to add them? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add $UNTRACKED
        echo "Added untracked files"
    fi
fi

# Get current version from manifest.json
current_version=$(jq -r '.version' custom_components/minertimer/manifest.json)

# Parse version components
IFS='.' read -r major minor patch <<< "$current_version"

# Increment based on argument
case "$1" in
  major)
    major=$((major + 1))
    minor=0
    patch=0
    ;;
  minor)
    minor=$((minor + 1))
    patch=0
    ;;
  patch)
    patch=$((patch + 1))
    ;;
  *)
    echo "Usage: $0 {major|minor|patch}"
    exit 1
    ;;
esac

# Create new version string
new_version="$major.$minor.$patch"

# Update manifest.json
jq ".version = \"$new_version\"" custom_components/minertimer/manifest.json > tmp.$$ && mv tmp.$$ custom_components/minertimer/manifest.json

# Update hacs.json
jq ".version = \"$new_version\"" hacs.json > tmp.$$ && mv tmp.$$ hacs.json

# Git operations
git add custom_components/minertimer/manifest.json hacs.json
git commit -m "Bump version to $new_version"
git tag -a "v$new_version" -m "Version $new_version"
git push && git push --tags

echo "Version bumped to $new_version"
echo "Changes committed and tagged as v$new_version" 