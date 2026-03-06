# Progressive Disclosure Guide

When and how to split skill content into multiple files for optimal performance.

## The 500-Line Guideline

**Goal**: Keep SKILL.md body under 500 lines for optimal performance.

**Warning Threshold**: 400 lines - start considering splitting
**Hard Limit**: 500 lines - should definitely split

**Why 500 lines?**
- Optimal token usage
- Faster loading
- Better context management
- Easier maintenance

## Decision Tree: To Split or Not To Split

```
Is SKILL.md body > 400 lines?
├─ NO → Keep together
│   └─ Mention threshold for future reference
│
└─ YES → Consider splitting
    │
    ├─ Are there distinct domains?
    │   (e.g., finance, sales, product data)
    │   └─ YES → Split by domain
    │       Example: reference/FINANCE.md, reference/SALES.md
    │
    ├─ Is there extensive API documentation?
    │   └─ YES → Move to reference/API_REFERENCE.md
    │
    ├─ Are there many examples (>50 lines)?
    │   └─ YES → Move to reference/EXAMPLES.md
    │
    ├─ Are there advanced features separate from core?
    │   └─ YES → Move to reference/ADVANCED_FEATURES.md
    │
    └─ Is there detailed troubleshooting (>30 lines)?
        └─ YES → Move to reference/TROUBLESHOOTING.md
```

## What to Keep in SKILL.md

**Always keep** (main workflow hub):
- YAML frontmatter
- Overview / Quick start
- Workflow steps (high-level, 1-2 lines per step)
- Quick reference for common operations
- Links to detailed guides
- Implementation guidelines (summary)
- Core examples (1-2, keep brief)

**Approximate line budget**:
- Frontmatter: 5 lines
- Overview: 20-30 lines
- Workflow steps: 100-150 lines
- Implementation guidelines: 50-80 lines
- Examples: 30-50 lines
- Notes: 10-20 lines
- **Total: ~300-400 lines**

## What to Move to Reference Files

**Move when exceeding thresholds**:

### 1. Domain-Specific Content (by domain)

**When**: Multiple distinct domains (finance, sales, product)

**Structure**:
```
reference/
├── FINANCE.md       # Finance domain schemas and queries
├── SALES.md         # Sales domain schemas and queries
└── PRODUCT.md       # Product domain schemas and queries
```

**SKILL.md links**:
```markdown
## Available Domains

**Finance**: Revenue, ARR, billing → See [reference/FINANCE.md](reference/FINANCE.md)
**Sales**: Opportunities, pipeline, accounts → See [reference/SALES.md](reference/SALES.md)
**Product**: API usage, features, adoption → See [reference/PRODUCT.md](reference/PRODUCT.md)
```

**Benefits**:
- The AI agent loads only relevant domain
- Easy to update specific domain
- Clear separation of concerns
- Scalable (add more domains easily)

### 2. API Reference Documentation

**When**: Extensive API documentation (>100 lines)

**What to move**:
- Complete API method signatures
- Parameter descriptions
- Response formats
- Error codes

**Keep in SKILL.md**:
- Quick reference (top 3-5 methods)
- Link to full reference

**Structure**:
```markdown
## Quick API Reference

Top methods:
- `method1()`: Brief description
- `method2()`: Brief description

For complete API reference, see [reference/API_REFERENCE.md](reference/API_REFERENCE.md)
```

### 3. Examples

**When**: Many examples (>50 lines total)

**What to move**:
- Detailed examples with explanations
- Edge cases
- Complex scenarios

**Keep in SKILL.md**:
- 1-2 simple examples showing basic usage

**Structure**:
```markdown
## Examples

**Basic usage**:
```bash
/skill-name simple-input.txt
```

For more examples including edge cases and complex scenarios, see [reference/EXAMPLES.md](reference/EXAMPLES.md)
```

### 4. Advanced Features

**When**: Advanced features separate from core workflow (>80 lines)

**What to move**:
- Configuration options
- Performance tuning
- Advanced patterns
- Optional integrations

**Keep in SKILL.md**:
- Core workflow only
- Link to advanced features

### 5. Troubleshooting

**When**: Extensive troubleshooting guide (>30 lines)

**What to move**:
- Common errors and solutions
- Debugging steps
- Known issues
- Workarounds

**Keep in SKILL.md**:
- Top 2-3 most common errors in error handling table

## Migration Pattern

### Before (600-line SKILL.md)

```markdown
---
name: bigquery-analysis
description: ...
---

# BigQuery Analysis

## Quick Start
[50 lines]

## Finance Domain
### Finance Schemas
[150 lines of table definitions]
### Finance Queries
[50 lines]

## Sales Domain
### Sales Schemas
[150 lines]
### Sales Queries
[50 lines]

## Product Domain
### Product Schemas
[150 lines]
### Product Queries
[50 lines]

Total: ~650 lines
```

### After (300-line SKILL.md + reference files)

**SKILL.md** (300 lines):
```markdown
---
name: bigquery-analysis
description: ...
---

# BigQuery Analysis

## Quick Start
[50 lines]

## Available Domains

**Finance**: Revenue, ARR, billing metrics
→ See [reference/FINANCE.md](reference/FINANCE.md)

**Sales**: Opportunities, pipeline, accounts
→ See [reference/SALES.md](reference/SALES.md)

**Product**: API usage, features, adoption
→ See [reference/PRODUCT.md](reference/PRODUCT.md)

## Quick Schema Search

Find specific schemas:
```bash
grep -i "revenue" reference/FINANCE.md
grep -i "pipeline" reference/SALES.md
grep -i "api_calls" reference/PRODUCT.md
```

## Workflow
[150 lines of high-level workflow]

## Implementation Guidelines
[50 lines]

Total: ~300 lines
```

**reference/FINANCE.md** (200 lines):
```markdown
# Finance Domain

## Overview
[Finance-specific context]

## Schemas
[150 lines of table definitions]

## Common Queries
[50 lines of query examples]
```

**Benefits**:
- SKILL.md: 300 lines (well under limit)
- Domain files loaded only when needed
- Easy to maintain and update
- Scales to more domains

## Reference File Organization

### Naming Conventions

**Use UPPERCASE for major reference files**:
- `EXAMPLES.md`
- `API_REFERENCE.md`
- `ADVANCED_FEATURES.md`
- `TROUBLESHOOTING.md`

**Use descriptive names for domain files**:
- `FINANCE.md` (not `domain1.md`)
- `SALES.md` (not `file2.md`)
- `PRODUCT.md` (not `stuff.md`)

### Keep One Level Deep

**Good** (one level from SKILL.md):
```
SKILL.md → reference/FINANCE.md
SKILL.md → reference/EXAMPLES.md
SKILL.md → reference/API_REFERENCE.md
```

**Bad** (nested references):
```
SKILL.md → reference/ADVANCED.md → reference/details/NESTED.md
```

**Why**: The AI agent may only partially read nested references

### Reference File Structure

Each reference file should have:

**1. Table of Contents** (for files >100 lines):
```markdown
# Domain Name

## Contents
- Section 1
- Section 2
- Section 3
```

**2. Clear Sections**:
```markdown
## Section 1: Overview

## Section 2: Schemas

## Section 3: Examples
```

**3. Self-Contained Content**:
- Don't assume reader has seen SKILL.md
- Include context for the domain/topic
- Cross-reference back to SKILL.md if needed

## When NOT to Split

**Don't split if**:
- SKILL.md is under 400 lines
- Content is highly interconnected (hard to separate)
- Splitting would make workflow harder to follow
- You have only one domain/topic

**Keep together when**:
- Workflow is sequential and splitting would break flow
- Examples are integral to understanding steps
- Content is already concise and well-organized

## Progressive Disclosure Benefits

**Token Efficiency**:
- Only relevant content loaded
- Reduces context window usage
- Faster response generation

**Maintainability**:
- Update specific domains independently
- Add new domains without touching core
- Clear ownership of content sections

**Scalability**:
- Easy to add more domains
- No limit on total content (just per-file)
- Grows naturally with needs

**User Experience**:
- Faster skill loading
- Focused content delivery
- Clear navigation structure

## Testing Your Split

After splitting, verify:

1. **SKILL.md under 500 lines**: ✓
2. **Links work**: Click each reference link
3. **One level deep**: No nested references
4. **The AI agent can navigate**: Test with real queries
5. **Content makes sense**: Each file is self-contained

## Example Splits by Use Case

### Use Case 1: API Skill with Many Endpoints

**Before**: 800 lines (all endpoints in SKILL.md)

**After**:
- SKILL.md (350 lines): Overview, top 5 endpoints, workflow
- reference/API_REFERENCE.md (450 lines): Complete endpoint documentation

### Use Case 2: Multi-Domain Data Analysis

**Before**: 650 lines (all domains together)

**After**:
- SKILL.md (300 lines): Overview, domain navigation, workflow
- reference/FINANCE.md (200 lines)
- reference/SALES.md (150 lines)
- reference/PRODUCT.md (200 lines)

### Use Case 3: Workflow with Many Examples

**Before**: 550 lines (examples embedded throughout)

**After**:
- SKILL.md (400 lines): Workflow with 2 basic examples
- reference/EXAMPLES.md (150 lines): All examples with detailed explanations

## Quick Reference Table

| Signal | Action | Result |
|--------|--------|--------|
| <400 lines | Keep together | No split needed |
| 400-500 lines | Consider splitting | Warning threshold |
| >500 lines | Split content | Required |
| Multiple domains | Split by domain | One file per domain |
| Extensive API docs | Move to reference | API_REFERENCE.md |
| Many examples | Move to reference | EXAMPLES.md |
| Advanced features | Move to reference | ADVANCED_FEATURES.md |

## Summary

**Golden Rule**: Keep SKILL.md as a navigation hub, move details to reference files.

**Process**:
1. Write skill content naturally
2. Count lines in SKILL.md body
3. If >400 lines, identify separable sections
4. Move sections to reference files
5. Update SKILL.md with links
6. Test navigation and discovery
