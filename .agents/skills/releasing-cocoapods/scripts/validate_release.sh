#!/bin/bash

# validate_release.sh - Validates current state for CocoaPods release
# Usage: ./scripts/validate_release.sh [podspec-name] [version]

set -e

PODSPEC=${1:-"*.podspec"}
VERSION=${2:-""}

echo "🔍 CocoaPods Release Validation"
echo "================================"

# Check if we're in a git repo
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Find podspec file
PODSPEC_FILE=$(ls *.podspec 2>/dev/null | head -n1)
if [ -z "$PODSPEC_FILE" ]; then
    echo "❌ Error: No .podspec file found in current directory"
    exit 1
fi

echo "📄 Found podspec: $PODSPEC_FILE"

# Extract current version from podspec
CURRENT_VERSION=$(grep "s.version\s*=" "$PODSPEC_FILE" | sed "s/.*'\([^']*\)'.*/\1/")
echo "📦 Current podspec version: $CURRENT_VERSION"

# If version specified, check if it matches
if [ -n "$VERSION" ] && [ "$VERSION" != "$CURRENT_VERSION" ]; then
    echo "⚠️  Warning: Specified version ($VERSION) differs from podspec ($CURRENT_VERSION)"
fi

# Check if podspec uses tag (not branch)
if grep -q ":branch.*=>" "$PODSPEC_FILE"; then
    echo "❌ Error: Podspec still uses :branch instead of :tag"
    echo "   Change: :branch => 'master' to :tag => s.version"
    exit 1
fi

echo "✅ Podspec uses :tag => s.version"

# Check git status
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: Uncommitted changes detected"
    git status --short
else
    echo "✅ Working directory clean"
fi

# Check if tag exists locally
TAG_VERSION=${VERSION:-$CURRENT_VERSION}
if git rev-parse "$TAG_VERSION" >/dev/null 2>&1; then
    echo "✅ Git tag $TAG_VERSION exists locally"
else
    echo "❌ Error: Git tag $TAG_VERSION does not exist locally"
    echo "   Run: git tag $TAG_VERSION"
    exit 1
fi

# Check if tag exists on remote
if git ls-remote --tags origin "$TAG_VERSION" | grep -q "$TAG_VERSION"; then
    echo "✅ Git tag $TAG_VERSION exists on remote"
else
    echo "❌ Error: Git tag $TAG_VERSION not found on remote"
    echo "   Run: git push origin $TAG_VERSION"
    exit 1
fi

# Check if CocoaPods CLI is available
if command -v pod >/dev/null 2>&1; then
    echo "✅ CocoaPods CLI available"
else
    echo "❌ Error: CocoaPods CLI not found"
    echo "   Install: sudo gem install cocoapods"
    exit 1
fi

# Check trunk registration
if pod trunk me >/dev/null 2>&1; then
    echo "✅ CocoaPods trunk session active"
else
    echo "⚠️  Warning: No active trunk session"
    echo "   Run: pod trunk register email@example.com 'Your Name'"
fi

echo ""
echo "🎉 Validation complete!"
echo "   Ready to run: pod spec lint $PODSPEC_FILE --allow-warnings"
