# Validation Scripts Reference

All scripts are in the [scripts/](../scripts/) directory and provide clear error messages with exit codes.

## validate_name.py

Validates skill names against all naming rules.

```bash
python scripts/validate_name.py "processing-pdfs"
# Output: ✓ Name valid: processing-pdfs
# Exit: 0

python scripts/validate_name.py "ProcessingPDFs"
# Output: ✗ Name invalid: Must use lowercase letters, numbers, hyphens only
# Exit: 1

python scripts/validate_name.py "--bad-name"
# Output: ✗ Name invalid: Name must not start with a hyphen
# Exit: 1

python scripts/validate_name.py "bad--name"
# Output: ✗ Name invalid: Name must not contain consecutive hyphens (--)
# Exit: 1
```

**Rules enforced**:
- Maximum 64 characters
- Lowercase letters, numbers, hyphens only
- Gerund form required (first segment must end in -ing)
- No start/end with hyphens
- No consecutive hyphens (--)
- No XML characters (<, >, &)
- No reserved words ("anthropic", "claude")

## validate_description.py

Validates skill descriptions against all description rules.

```bash
python scripts/validate_description.py "Processes PDF files..."
# Output: ✓ Description valid (45 characters)
# Exit: 0

python scripts/validate_description.py ""
# Output: ✗ Description invalid: Cannot be empty
# Exit: 1

python scripts/validate_description.py "I help you process PDFs"
# Output: ✗ Description invalid: Description must be in third person (found: I, you)
# Exit: 1
```

**Rules enforced**:
- Maximum 1024 characters
- Non-empty
- No XML characters
- Third person only (no "I", "you", "we", "your", "our")
- Warns if missing "when to use" guidance

## validate_frontmatter.py

Validates both name and description from YAML frontmatter in a SKILL.md file.

```bash
python scripts/validate_frontmatter.py /path/to/SKILL.md
# Validates both name and description from YAML frontmatter
# Exit: 0 if valid, 1 if invalid
```

## create_skill_structure.py

Creates a complete skill directory structure with validated inputs.

```bash
python scripts/create_skill_structure.py \
  --name "processing-pdfs" \
  --description "Processes PDF files..." \
  --template "basic" \
  --output-dir ".agents/skills/processing-pdfs"
```

**Template types**:
- `basic` — Text-only workflows, no scripts
- `scripts` — Includes scripts/ directory for utilities
- `progressive` — Includes reference/ directory for detailed docs

**What it creates**:
- Skill directory with validated SKILL.md
- Subdirectories based on template type
- reference/IMPROVEMENTS.md for self-improvement tracking

## JSON Output

All validation scripts support `--json` flag for programmatic use:

```bash
python scripts/validate_name.py "processing-pdfs" --json
# Output: {"valid": true, "name": "processing-pdfs", "errors": []}
```
