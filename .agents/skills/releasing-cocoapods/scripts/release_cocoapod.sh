#!/bin/bash

# release_cocoapod.sh - Automated CocoaPods release script
# Usage: ./scripts/release_cocoapod.sh [version] [podspec-name]

set -e

VERSION=${1:-""}
PODSPEC=${2:-"*.podspec"}

echo "🚀 CocoaPods Release Automation"
echo "==============================="

# Find podspec file if not specified
if [ "$PODSPEC" = "*.podspec" ]; then
    PODSPEC_FILE=$(ls *.podspec 2>/dev/null | head -n1)
    if [ -z "$PODSPEC_FILE" ]; then
        echo "❌ Error: No .podspec file found"
        exit 1
    fi
else
    PODSPEC_FILE=$PODSPEC
fi

echo "📄 Using podspec: $PODSPEC_FILE"

# Extract current version if not specified
if [ -z "$VERSION" ]; then
    CURRENT_VERSION=$(grep "s.version\s*=" "$PODSPEC_FILE" | sed "s/.*'\([^']*\)'.*/\1/")
    echo "📦 Current version: $CURRENT_VERSION"
    echo "🔢 Enter new version (or press Enter to use $CURRENT_VERSION):"
    read -r INPUT_VERSION
    VERSION=${INPUT_VERSION:-$CURRENT_VERSION}
fi

echo "🎯 Releasing version: $VERSION"

# Step 1: Update podspec
echo ""
echo "📝 Step 1: Updating podspec..."
sed -i.bak "s/s.version\s*=\s*'.*'/s.version = '$VERSION'/" "$PODSPEC_FILE"
echo "✅ Updated version to $VERSION"

# Ensure source uses tag
if grep -q ":branch.*=>" "$PODSPEC_FILE"; then
    sed -i.bak 's/:branch.*=>.*master/:tag => s.version/' "$PODSPEC_FILE"
    echo "✅ Changed source to use :tag => s.version"
fi

# Step 2: Commit changes
echo ""
echo "📤 Step 2: Committing changes..."
git add "$PODSPEC_FILE"
git commit -m "Bump podspec to $VERSION"
echo "✅ Changes committed"

# Step 3: Push to remote
echo ""
echo "📡 Step 3: Pushing to remote..."
git push origin master
echo "✅ Pushed to origin/master"

# Step 4: Create and push tag
echo ""
echo "🏷️  Step 4: Creating and pushing tag..."
git tag "$VERSION"
git push origin "$VERSION"
echo "✅ Tag $VERSION created and pushed"

# Step 5: Validate podspec
echo ""
echo "🔍 Step 5: Validating podspec..."
if pod spec lint "$PODSPEC_FILE" --allow-warnings; then
    echo "✅ Podspec validation passed"
else
    echo "❌ Podspec validation failed"
    exit 1
fi

# Step 6: Check trunk registration
echo ""
echo "👤 Step 6: Checking trunk registration..."
if ! pod trunk me >/dev/null 2>&1; then
    echo "⚠️  No trunk session found"
    echo "📧 Enter email for trunk registration:"
    read -r EMAIL
    echo "👤 Enter your name:"
    read -r NAME
    pod trunk register "$EMAIL" "$NAME"
    echo "📧 Check your email for verification link"
    echo "⏳  Press Enter after verifying email..."
    read -r
fi

# Step 7: Push to CocoaPods
echo ""
echo "🎯 Step 7: Pushing to CocoaPods..."
if pod trunk push "$PODSPEC_FILE" --allow-warnings; then
    echo ""
    echo "🎉 SUCCESS! $PODSPEC_FILE version $VERSION published to CocoaPods"
    echo "🌍 https://cocoapods.org/pods/$(basename "$PODSPEC_FILE" .podspec)"
else
    echo "❌ Failed to push to CocoaPods"
    exit 1
fi

# Cleanup
rm -f "$PODSPEC_FILE.bak"

echo ""
echo "✨ Release complete!"
