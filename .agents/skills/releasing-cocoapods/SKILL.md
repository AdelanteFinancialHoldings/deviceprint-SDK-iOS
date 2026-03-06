---
name: releasing-cocoapods
description: Manages the complete CocoaPods release workflow including podspec updates, git tagging, validation, and trunk publishing. Use when releasing new versions to CocoaPods or when podspec version differs from published version. Do NOT use for general git operations or package management for other platforms (use appropriate skills instead).
compatibility: Designed for AI coding agents with Bash and file system access, requires CocoaPods CLI and git
metadata:
  author: AI Agent
  mcp-server: git
---

# Releasing CocoaPods

Manages the complete workflow for publishing new versions to CocoaPods with proper git tagging and validation.

## Quick Start

For a standard release, the AI agent will:

1. Update podspec version and source to use git tag
2. Commit and push changes to git
3. Create and push git tag
4. Validate with `pod spec lint`
5. Handle trunk registration if needed
6. Push to CocoaPods trunk

## Release Workflow

### Step 1: Update Podspec

**Critical Changes Required**:

- Update `s.version` to the new version number
- Change `s.source` from `:branch => 'master'` to `:tag => s.version`

**Example Changes**:

```ruby
# Before
s.version = '5.7.0'
s.source = { :git => 'https://github.com/user/repo.git', :branch => 'master' }

# After
s.version = '5.8.0'
s.source = { :git => 'https://github.com/user/repo.git', :tag => s.version }
```

### Step 2: Commit and Push

```bash
git add [podspec-name].podspec
git commit -m "Bump podspec to [version]"
git push origin master
```

### Step 3: Create and Push Tag

```bash
git tag [version]
git push origin [version]
```

**Important**: The tag must exist on GitHub BEFORE pushing to CocoaPods trunk.

### Step 4: Validate Podspec

```bash
pod spec lint [podspec-name].podspec --allow-warnings
```

Fix any errors before proceeding. Common issues:

- Missing git tag
- Invalid podspec syntax
- Missing required files

### Step 5: Check Trunk Registration

```bash
pod trunk me
```

If not registered:

```bash
pod trunk register email@example.com 'Your Name'
```

**Email Verification Required**: Click the link in the verification email.

### Step 6: Push to CocoaPods

```bash
pod trunk push [podspec-name].podspec --allow-warnings
```

## Validation Scripts

Use these scripts to verify each step:

### Check Current State

```bash
# Check current podspec version
grep "s.version" *.podspec

# Check current published version
pod trunk info [podspec-name]
```

### Validate Git Tag

```bash
# Verify tag exists locally
git tag -l [version]

# Verify tag exists on remote
git ls-remote --tags origin [version]
```

### Validate Podspec

```bash
# Full validation
pod spec lint [podspec-name].podspec --allow-warnings

# Quick syntax check
pod spec lint --quick [podspec-name].podspec
```

## Common Scenarios

### First-Time Release

1. Complete trunk registration with email verification
2. Ensure podspec uses `:tag => s.version` (not `:branch`)
3. Create initial git tag before pushing
4. Push to trunk - automatically becomes pod owner

### Emergency Patch Release

- Use semantic versioning (e.g., 5.8.1 for patch)
- Follow same workflow but emphasize speed
- Skip optional validations if time-critical

### Version Mismatch

When podspec version ≠ published version:

1. Check git log for unmerged release commits
2. Update podspec to match intended version
3. Create missing git tag if needed
4. Push to trunk

## Troubleshooting

### "No such file or directory" during lint

- Ensure you're in the correct directory
- Check podspec filename matches exactly

### "You need to run `pod trunk register`"

- Run `pod trunk register email@domain.com 'Name'`
- Check email for verification link
- Click link before proceeding

### "The source of a binary only pod should not be the HEAD of a branch"

- Change `:branch => 'master'` to `:tag => s.version`
- Create and push the git tag

### "tag not found" errors

- Verify tag exists: `git tag -l [version]`
- Push tag to remote: `git push origin [version]`
- Wait 1-2 minutes for GitHub to process

## Quality Checklist

Before publishing:

- [ ] Podspec version updated
- [ ] Source uses `:tag => s.version`
- [ ] Changes committed and pushed
- [ ] Git tag created and pushed
- [ ] `pod spec lint` passes
- [ ] Trunk session verified
- [ ] Email verified (if first time)

## Notes

- Always use `--allow-warnings` for non-critical warnings
- Git tags are required for CocoaPods releases
- Trunk registration is one-time per email
- Each version must have a unique git tag
- Consider using semantic versioning (MAJOR.MINOR.PATCH)
