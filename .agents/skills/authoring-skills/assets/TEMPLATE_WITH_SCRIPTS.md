# Template: Skill with Scripts

Use this template for skills that need validation, automation, or utility scripts.

**Good for**: PDF processing, database migrations, data validation, code generation

---

```markdown
---
name: your-skill-name
# Use gerund form (verb + -ing): processing-pdfs, analyzing-data
# Max 64 characters, lowercase, numbers, hyphens only
# Directory name must match this name field

description: Brief description of what the skill does and when to use it...
# Max 1024 characters, third person only
# Include WHAT and WHEN to use, plus WHEN NOT to use (negative triggers)

# Optional fields:
# compatibility: Designed for AI coding agents with Bash and file system access
# allowed-tools: "Bash(python:*) Read Write Edit"
# metadata:
#   author: your-team-name
#   mcp-server: server-name-if-applicable
---

# Your Skill Title

Brief overview including mention of automation/validation capabilities.

## Business Objective

Explain what this skill accomplishes and why scripts make it more reliable.

## Usage

```bash
/your-skill-name [input-file] [options]
```

**Arguments:**
- `input-file`: Input file to process
- `options`: Optional configuration

## Input Format

```
Example input format
```

## Task Workflow

Copy and track progress:

```
Progress:
- [ ] Step 1: Prepare input
- [ ] Step 2: Run validation script
- [ ] Step 3: Process data
- [ ] Step 4: Verify output
```

### Step 1: Prepare Input

Instructions for preparing input.

### Step 2: Run Validation Script

**Validate immediately** before processing:

```bash
python scripts/validate_input.py input-file.txt
```

**Expected output**:
- `✓ Input valid` (exit code 0) → Proceed
- `✗ Input invalid: [errors]` (exit code 1) → Fix and re-validate

**Common validation errors**:
- Error type 1: How to fix
- Error type 2: How to fix

**Do not proceed until validation passes.**

### Step 3: Process Data

Instructions for main processing.

**Use utility script for complex operations**:

```bash
python scripts/process_data.py input-file.txt output-file.txt
```

**Script behavior**:
- What the script does
- What output it produces
- How errors are handled

### Step 4: Verify Output

**Run verification script**:

```bash
python scripts/verify_output.py output-file.txt
```

If verification fails:
1. Review error messages
2. Check intermediate files
3. Re-run with debug flag: `--debug`
4. Fix issues and repeat Step 3

## Utility Scripts

All scripts are in the `scripts/` directory.

### validate_input.py

**Purpose**: Validate input file format and content

**Usage**:
```bash
python scripts/validate_input.py <input-file>
```

**Exit codes**:
- 0: Valid input
- 1: Invalid input (with specific error messages)

**What it checks**:
- Check 1 description
- Check 2 description
- Check 3 description

### process_data.py

**Purpose**: Main processing script

**Usage**:
```bash
python scripts/process_data.py <input> <output> [--option value]
```

**Options**:
- `--option value`: Description of option

**Output**: Description of what gets created

**Error handling**:
- How the script handles errors
- What happens on failure
- How to recover

### verify_output.py

**Purpose**: Verify output correctness

**Usage**:
```bash
python scripts/verify_output.py <output-file>
```

**Verification checks**:
- Check 1: Description
- Check 2: Description
- Check 3: Description

**Exit codes**:
- 0: Output valid
- 1: Output invalid (with specific issues)

## Implementation Guidelines

**Workflow Pattern: Validate → Process → Verify**

Always follow this sequence:
1. Validate input (catch errors early)
2. Process data (reliable script execution)
3. Verify output (ensure correctness)

**Use TodoWrite for Progress Tracking**

**Error Handling**:

| Error | Action |
|-------|--------|
| Validation fails | Fix input, re-validate, do not proceed |
| Processing fails | Check error message, review input, retry |
| Verification fails | Review output, check logs, re-run process |
| Script not found | Check scripts/ directory exists |

**Efficiency**:
- Scripts are executed (not loaded into context)
- Only script output consumes tokens
- Cache intermediate results when possible
- Run independent scripts in parallel

## Script Development Guidelines

**When creating utility scripts**:

1. **Solve, don't punt**: Handle errors explicitly
2. **Clear error messages**: Tell user exactly what's wrong
3. **Exit codes**: 0 for success, 1 for failure
4. **Documentation**: Include usage in docstring
5. **Validation**: Check inputs before processing

**Good script example**:
```python
#!/usr/bin/env python3
"""Validate input file format.

Usage: python validate_input.py <file>
Exit: 0 if valid, 1 if invalid
"""

def validate(filepath):
    try:
        # Validation logic with clear error messages
        pass
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return False
    except ValueError as e:
        print(f"Error: Invalid format: {e}")
        return False
    return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python validate_input.py <file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    sys.exit(0 if result else 1)
```

## Examples

**Example 1: Happy path**
```bash
/your-skill-name input.txt

Step 1: Prepared input
Step 2: ✓ Validation passed
Step 3: Processing... ✓ Complete
Step 4: ✓ Verification passed

Output: output.txt
```

**Example 2: Validation catches error**
```bash
/your-skill-name invalid-input.txt

Step 2: ✗ Validation failed
  - Error: Missing required field 'name'
  - Fix the input and re-run validation
```

**Example 3: With options**
```bash
/your-skill-name input.txt --format json

Step 2: ✓ Validation passed
Step 3: Processing with JSON format... ✓ Complete
Step 4: ✓ Verification passed
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| [Common error 1] | [Root cause] | [How to resolve] |
| [Common error 2] | [Root cause] | [How to resolve] |
| [Common error 3] | [Root cause] | [How to resolve] |

## Final Step: Collect Feedback (Self-Improvement)

**IMPORTANT**: After completing this task, gather feedback to improve this skill.

Ask the user:
1. "Did anything go wrong during this process?"
2. "What could be improved about these instructions?"
3. "Did the validation scripts work correctly?"
4. "Were any steps unclear or missing?"
5. "Did the workflow match your expectations?"

### Learning Mode Self-Improvement

If issues or improvements are identified:

**Document the Feedback**:
- Issue description
- Context: When and how it occurred
- Which step or script was affected
- Proposed improvement

**Log Proposed Improvement** (DO NOT automatically apply changes):

Append to [reference/IMPROVEMENTS.md](reference/IMPROVEMENTS.md):

\`\`\`markdown
## [Date] - Proposed Improvement #N

**Issue**: [Description of what went wrong]
**Context**: [When and how it occurred]
**Affected Component**: [Step/script name]

**Proposed Changes**:
- File: SKILL.md or scripts/script_name.py
  - What should be changed
  - Why this would help

**Status**: PENDING MANUAL REVIEW

**Expected Result**: [What this would improve]
\`\`\`

**Notify User**:
"I've logged a proposed improvement in reference/IMPROVEMENTS.md. You can review and apply it manually when you're ready."

**Benefits of Learning Mode**:
- Scripts can be improved based on real usage
- Validation logic can be enhanced
- Error handling can be refined
- Skill gets more reliable over time

## Business Value

- **Reliability**: Scripts ensure consistent, correct processing
- **Efficiency**: Automated validation catches errors early
- **Quality**: Verification ensures output meets requirements
- **Self-improvement**: Skill and scripts improve based on actual usage patterns

## Notes

- Always validate before processing
- Scripts provide deterministic behavior
- Use scripts for fragile operations
- Verification is not optional
- Keep scripts focused and single-purpose
- **Self-Improvement**: Collect feedback after each use to refine scripts and workflow
```

## Template Usage Guide

**When to use this template**:
- Tasks requiring validation
- Automation of complex operations
- Data processing pipelines
- Operations where consistency is critical

**Scripts to include**:
- Validation scripts (check inputs)
- Processing scripts (main logic)
- Verification scripts (check outputs)
- Utility scripts (helper functions)

**Directory structure**:
```
your-skill/
├── SKILL.md
└── scripts/
    ├── validate_input.py
    ├── process_data.py
    ├── verify_output.py
    └── README.md
```
