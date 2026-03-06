# CocoaPods Release Scripts

Utility scripts to automate and validate CocoaPods releases.

## Scripts

### validate_release.sh

Validates the current state before attempting a CocoaPods release.

**Usage:**

```bash
./scripts/validate_release.sh [podspec-name] [version]
```

**What it checks:**

- Git repository status
- Podspec file existence and version
- Source configuration (must use `:tag => s.version`)
- Git tag existence (local and remote)
- CocoaPods CLI availability
- Trunk registration status

**Examples:**

```bash
# Validate with auto-detected podspec and version
./scripts/validate_release.sh

# Validate specific podspec and version
./scripts/validate_release.sh MyLib.podspec 1.2.0
```

### release_cocoapod.sh

Automated script for complete CocoaPods release workflow.

**Usage:**

```bash
./scripts/release_cocoapod.sh [version] [podspec-name]
```

**What it does:**

1. Updates podspec version and source configuration
2. Commits and pushes changes to git
3. Creates and pushes git tag
4. Runs `pod spec lint` validation
5. Checks/sets up trunk registration
6. Pushes to CocoaPods trunk

**Examples:**

```bash
# Interactive release with auto-detected version
./scripts/release_cocoapod.sh

# Direct release with specific version
./scripts/release_cocoapod.sh 1.2.0

# Release specific podspec
./scripts/release_cocoapod.sh 1.2.0 MyLib.podspec
```

## Requirements

- Git repository with a `.podspec` file
- CocoaPods CLI installed (`gem install cocoapods`)
- Active internet connection for git and CocoaPods operations
- Email access for trunk verification (first-time setup)

## Notes

- Scripts create backup files (`.bak`) that are cleaned up after successful release
- Always use `--allow-warnings` for non-critical lint warnings
- Git tags must exist on remote before CocoaPods trunk push
- Trunk registration is one-time per email address
