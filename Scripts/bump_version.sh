#!/bin/bash

# Check if version type is provided
if [ -z "$1" ]; then
    echo "Usage: $0 [major|minor|patch]"
    exit 1
fi

# Function to increment version number
increment_version() {
    local version=$1
    local type=$2
    
    IFS='.' read -ra parts <<< "$version"
    case $type in
        major)
            ((parts[0]++))
            parts[1]=0
            parts[2]=0
            ;;
        minor)
            ((parts[1]++))
            parts[2]=0
            ;;
        patch)
            ((parts[2]++))
            ;;
        *)
            echo "Invalid version type. Use major, minor, or patch"
            exit 1
            ;;
    esac
    
    echo "${parts[0]}.${parts[1]}.${parts[2]}"
}

# Get current version from manifest.json
CURRENT_VERSION=$(grep '"version":' custom_components/minertimer/manifest.json | sed 's/.*: "\(.*\)".*/\1/')
NEW_VERSION=$(increment_version $CURRENT_VERSION $1)

echo "Updating version from $CURRENT_VERSION to $NEW_VERSION"

# Update version in manifest.json
sed -i '' "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" custom_components/minertimer/manifest.json

# Update version in hacs.json
sed -i '' "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" hacs.json

# Commit changes
git add custom_components/minertimer/manifest.json hacs.json
git commit -m "Bump version to $NEW_VERSION"

# Create and push tag
git tag -a "v$NEW_VERSION" -m "Version $NEW_VERSION"
git push && git push --tags

echo "Version bump complete!"
echo "New version v$NEW_VERSION has been committed and tagged" 