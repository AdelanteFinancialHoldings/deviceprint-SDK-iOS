# Template: Progressive Disclosure Skill

Use this template for complex skills approaching or exceeding the 500-line limit.

**Good for**: Multi-domain analysis (finance, sales, product), comprehensive API skills, large reference documentation

---

```markdown
---
name: your-skill-name
# Use gerund form (verb + -ing): processing-pdfs, analyzing-data
# Max 64 characters, lowercase, numbers, hyphens only
# Directory name must match this name field

description: Brief description mentioning the multiple domains or features covered...
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

High-level overview that explains the scope without diving into details.

## Available Domains/Features

**Domain 1**: Brief description → See [reference/DOMAIN1.md](reference/DOMAIN1.md)
**Domain 2**: Brief description → See [reference/DOMAIN2.md](reference/DOMAIN2.md)
**Domain 3**: Brief description → See [reference/DOMAIN3.md](reference/DOMAIN3.md)

## Quick Search

Find specific information quickly:

```bash
# Search for specific term in domain 1
grep -i "search-term" reference/DOMAIN1.md

# Search across all domains
grep -i "search-term" reference/*.md
```

## Quick Start

### Common Task 1

Brief instructions with link to details:

```bash
/your-skill-name task1 input
```

For detailed guidance, see [reference/DOMAIN1.md](reference/DOMAIN1.md)

### Common Task 2

Brief instructions with link to details:

```bash
/your-skill-name task2 input
```

For detailed guidance, see [reference/DOMAIN2.md](reference/DOMAIN2.md)

## Task Workflow

Copy and track progress:

```
Progress:
- [ ] Step 1: Determine domain
- [ ] Step 2: Read relevant reference file
- [ ] Step 3: Execute domain-specific workflow
- [ ] Step 4: Generate output
```

### Step 1: Determine Domain

Based on user request, identify which domain applies:

- **Keywords for Domain 1**: keyword1, keyword2, keyword3
- **Keywords for Domain 2**: keyword4, keyword5, keyword6
- **Keywords for Domain 3**: keyword7, keyword8, keyword9

### Step 2: Read Relevant Reference File

**For Domain 1 tasks**: Read [reference/DOMAIN1.md](reference/DOMAIN1.md)
**For Domain 2 tasks**: Read [reference/DOMAIN2.md](reference/DOMAIN2.md)
**For Domain 3 tasks**: Read [reference/DOMAIN3.md](reference/DOMAIN3.md)

The AI agent loads only the relevant domain file (saves context tokens).

### Step 3: Execute Domain-Specific Workflow

Follow the workflow in the relevant reference file.

Each domain file includes:
- Specific schema/structure information
- Domain-specific patterns
- Examples for that domain
- Common queries or operations

### Step 4: Generate Output

Create output following the domain-specific format.

## Implementation Guidelines

**Progressive Disclosure Benefits**:
- SKILL.md stays under 500 lines (optimal performance)
- Domain files loaded only when needed (token efficiency)
- Easier to maintain and update specific domains
- Clear separation of concerns

**Use TodoWrite for Progress Tracking**

**Error Handling**:

| Error | Action |
|-------|--------|
| Ambiguous domain | Ask user to clarify |
| Reference file not found | List available domains |
| Multiple domains needed | Process sequentially |

**Efficiency**:
- Load only relevant reference files
- Cache domain information if processing multiple items
- Use grep for quick lookups across domains

## Organization Pattern

**SKILL.md** (this file):
- High-level overview
- Domain navigation
- Quick search patterns
- Common workflows

**reference/DOMAIN1.md**:
- Complete domain 1 documentation
- Schemas, examples, patterns
- Domain-specific workflows

**reference/DOMAIN2.md**:
- Complete domain 2 documentation
- Schemas, examples, patterns
- Domain-specific workflows

**reference/DOMAIN3.md**:
- Complete domain 3 documentation
- Schemas, examples, patterns
- Domain-specific workflows

## Examples

**Example 1: Single domain**
```bash
/your-skill-name domain1-query

Step 1: Identified Domain 1
Step 2: Read reference/DOMAIN1.md
Step 3: Executed domain 1 workflow
Step 4: Generated output
```

**Example 2: Cross-domain**
```bash
/your-skill-name cross-domain-query

Step 1: Identified Domains 1 and 2
Step 2: Read reference/DOMAIN1.md and reference/DOMAIN2.md
Step 3: Executed combined workflow
Step 4: Generated unified output
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
3. "Were the domain reference files helpful?"
4. "Should any content be reorganized?"
5. "Were any steps unclear or missing?"

### Learning Mode Self-Improvement

If issues or improvements are identified:

**Document the Feedback**:
- Issue description
- Context: When and how it occurred
- Which domain or step was affected
- Proposed improvement

**Log Proposed Improvement** (DO NOT automatically apply changes):

Append to [reference/IMPROVEMENTS.md](reference/IMPROVEMENTS.md):

\`\`\`markdown
## [Date] - Proposed Improvement #N

**Issue**: [Description of what went wrong]
**Context**: [When and how it occurred]
**Affected Component**: [Domain name or step]

**Proposed Changes**:
- File: SKILL.md or reference/DOMAIN.md
  - What should be changed
  - Why this would help

**Status**: PENDING MANUAL REVIEW

**Expected Result**: [What this would improve]
\`\`\`

**Notify User**:
"I've logged a proposed improvement in reference/IMPROVEMENTS.md. You can review and apply it manually when you're ready."

**Benefits for Multi-Domain Skills**:
- Individual domains can be improved independently
- Navigation can be refined based on usage patterns
- New domains can be added based on requests
- Domain organization can evolve over time

## Business Value

- **Comprehensive coverage**: Multiple domains in one skill
- **Efficient**: Loads only relevant information
- **Maintainable**: Update specific domains independently
- **Scalable**: Easy to add new domains
- **Self-improvement**: Domains and navigation improve based on real usage

## Notes

- SKILL.md under 500 lines (navigation and overview only)
- Reference files contain complete domain documentation
- One level deep: SKILL.md → reference/FILE.md (no nesting)
- Use descriptive reference file names
- Keep each reference file focused on one domain/topic
- **Self-Improvement**: Collect feedback to refine domains and navigation over time
```

---

## Reference File Structure

Each reference file (e.g., `reference/DOMAIN1.md`) should follow this structure:

```markdown
# Domain 1: [Domain Name]

## Overview

What this domain covers.

## Table of Contents

- Core Concepts
- Schema/Structure
- Common Patterns
- Examples
- Troubleshooting

## Core Concepts

Key concepts specific to this domain.

## Schema/Structure

Detailed schema, data structure, or API reference for this domain.

```
Example schema:
{
  "field1": "description",
  "field2": "description"
}
```

## Common Patterns

### Pattern 1: [Pattern Name]

Description and usage.

```
Example code or query
```

### Pattern 2: [Pattern Name]

Description and usage.

## Examples

### Example 1: [Simple Case]

```
Example with explanation
```

### Example 2: [Complex Case]

```
More complex example
```

## Troubleshooting

Common issues and solutions:

| Issue | Solution |
|-------|----------|
| Issue 1 | How to fix |
| Issue 2 | How to fix |

## Notes

- Domain-specific notes
- Assumptions or limitations
```

## Template Usage Guide

**When to use this template**:
- SKILL.md would exceed 400-500 lines
- Multiple distinct domains or topics
- Extensive documentation or API reference
- Schema-heavy skills (database, API schemas)

**How to organize**:
1. Keep SKILL.md as navigation hub (under 500 lines)
2. One reference file per domain/topic
3. Use descriptive names: FINANCE.md, SALES.md, PRODUCT.md
4. Include table of contents in long reference files
5. Keep references one level deep (no subdirectories)

**Decision tree for splitting**:
- Different domains (finance vs sales) → Separate files
- Core vs advanced features → Separate files
- API reference (extensive) → Separate file
- Many examples → Separate EXAMPLES.md

**Don't forget**:
- Link clearly from SKILL.md to each reference file
- Make domain keywords obvious for discovery
- Test that references load correctly
- Keep each reference file focused
