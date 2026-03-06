# Template: Basic Skill (Text-Only Workflows)

Use this template for simple text-only workflows that don't require executable scripts.

**Good for**: Research synthesis, document review, analysis workflows, formatting guidance

---

```markdown
---
# YAML Frontmatter (required)
name: your-skill-name
# Use gerund form (verb + -ing): processing-pdfs, analyzing-data
# Max 64 characters, lowercase, numbers, hyphens only
# No reserved words: anthropic, claude
# Directory name must match this name field

description: Brief description of what the skill does and when to use it...
# Max 1024 characters, third person only
# Include WHAT the skill does AND WHEN to use it
# Include WHEN NOT to use it (negative triggers)
# Use specific key terms for discoverability

# Optional fields:
# compatibility: Designed for AI coding agents with Bash and file system access
# allowed-tools: "Bash(python:*) Read Write Edit"
# metadata:
#   author: your-team-name
#   mcp-server: server-name-if-applicable
---

# Your Skill Title

Brief overview of what this skill accomplishes.

## Business Objective

Explain the "why" - what business need does this address?
What value does this provide to users?

## Usage

```bash
/your-skill-name [argument1] [argument2]
```

**Arguments:**
- `argument1`: Description of first argument (if applicable)
- `argument2`: Description of second argument with default value (if applicable)

## Input Format

If your skill expects specific input format, show it here:

```
Example input format:
- Item 1
- Item 2
- Item 3
```

## Task Workflow

Copy and track progress:

```
Progress:
- [ ] Step 1: [First step description]
- [ ] Step 2: [Second step description]
- [ ] Step 3: [Third step description]
- [ ] Step 4: [Fourth step description]
```

### Step 1: [First Step Name]

Detailed instructions for the first step.

**What to do**:
1. Specific action 1
2. Specific action 2
3. Specific action 3

**Tips**:
- Important consideration or best practice
- Common pitfall to avoid

### Step 2: [Second Step Name]

Detailed instructions for the second step.

**Decision point**: If X, then do A. If Y, then do B.

**Pattern to follow**:
- Pattern element 1
- Pattern element 2

### Step 3: [Third Step Name]

Detailed instructions for the third step.

**Validation**: How to verify this step was completed correctly.

### Step 4: [Fourth Step Name]

Final step instructions.

**Output format**:
```
Expected output structure
```

## Implementation Guidelines

**Use TodoWrite for Progress Tracking**

Create todos for each step:
```
- Step 1: [step name]
- Step 2: [step name]
- Step 3: [step name]
- Step 4: [step name]
```

**Efficiency**:
- Tip for optimizing performance
- When to use parallel operations
- What to cache or reuse

**Error Handling**:

| Error | Action |
|-------|--------|
| Error type 1 | How to handle it |
| Error type 2 | How to handle it |
| Error type 3 | How to handle it |

**Validation**:

After completing the workflow:
1. Verification step 1
2. Verification step 2
3. Verification step 3

## Examples

**Example 1: [Simple case]**
```bash
/your-skill-name basic-input.txt
```

Expected result: Description of what happens

**Example 2: [Complex case]**
```bash
/your-skill-name complex-input.txt --option value
```

Expected result: Description of what happens with options

**Example 3: [Edge case]**
```bash
/your-skill-name edge-case-input.txt
```

Expected result: How edge cases are handled

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
3. "Were any steps unclear or missing?"
4. "Did the workflow match your expectations?"

### Learning Mode Self-Improvement

If issues or improvements are identified:

**Document the Feedback**:
- Issue description
- Context: When and how it occurred
- Which step was affected
- Proposed improvement

**Log Proposed Improvement** (DO NOT automatically apply changes):

Append to [reference/IMPROVEMENTS.md](reference/IMPROVEMENTS.md):

\`\`\`markdown
## [Date] - Proposed Improvement #N

**Issue**: [Description of what went wrong]
**Context**: [When and how it occurred]
**Affected Step**: [Step name/number]

**Proposed Changes**:
- File: SKILL.md (or other file)
  - What should be changed
  - Why this would help

**Status**: PENDING MANUAL REVIEW

**Expected Result**: [What this would improve]
\`\`\`

**Notify User**:
"I've logged a proposed improvement in reference/IMPROVEMENTS.md. You can review and apply it manually when you're ready."

**If No Issues**:
Still document success: "Session completed successfully, no improvements needed at this time."

**Benefits of Learning Mode**:
- Full user control over changes
- Review before implementation
- Track what works and what doesn't
- Skill improves over time based on real usage
- Build knowledge base of improvement proposals

## Business Value

This skill provides:
- **Value proposition 1**: Specific benefit
- **Value proposition 2**: Specific benefit
- **Value proposition 3**: Specific benefit
- **Self-improvement**: Learns from usage and gets better over time

## Notes

- Important note 1 about usage or behavior
- Important note 2 about limitations or assumptions
- Important note 3 about best practices
- **Self-Improvement**: Always collect feedback after completing tasks to enable skill improvement
```

## Template Usage Guide

**When to use this template**:
- Simple workflows without automation needs
- Analysis or research tasks
- Document formatting or review processes
- Guidance-only skills

**Customization tips**:
1. Replace all `[placeholder]` text with your specific content
2. Remove sections that don't apply to your skill
3. Add sections if needed for your specific use case
4. Keep the overall structure but adapt to your needs
5. Ensure SKILL.md stays under 500 lines

**Don't forget**:
- Validate name and description before creating
- Use concrete examples, not abstract ones
- Include a checklist workflow for complex tasks
- Add error handling guidance
- Test with real usage scenarios
