# Skill Authoring Best Practices (Offline Version)

**Snapshot Date**: 2026-02-05
**Source**: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md

**Note**: This is an offline snapshot for use when WebFetch fails. For the latest version, see the link above or use Step 1 of the authoring-skills workflow.

## Validation Rules

### Name Field (YAML Frontmatter)
- **Maximum length**: 64 characters
- **Allowed characters**: Lowercase letters (a-z), numbers (0-9), hyphens (-) only
- **No XML tags**: Cannot contain `<`, `>`, `&`, or other XML characters
- **No reserved words**: Cannot contain "anthropic" or "claude"
- **Not empty**: Required field

**Naming Rules**:
- Gerund form required (verb + -ing): `processing-pdfs`, `analyzing-spreadsheets`, `managing-databases`
- Rejected: noun phrases (`pdf-processing`, `spreadsheet-analysis`) — not gerund form
- Avoid: vague names (`helper`, `utils`, `tools`), overly generic (`documents`, `data`)

### Description Field (YAML Frontmatter)
- **Maximum length**: 1024 characters
- **Required**: Cannot be empty
- **No XML tags**: Cannot contain `<`, `>`, `&`, or other XML characters
- **Point of view**: MUST be in third person
  - Bad: "I help you process PDFs", "You can use this for..."
  - Good: "Processes PDF files and extracts text..."
- **Content requirements**:
  - Include WHAT the skill does
  - Include WHEN to use it (discovery keywords)
  - Be specific with key terms
  - Use concrete language, not vague

**Good Description Example**:
```yaml
description: Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

## Core Principles

### 1. Concise is Key

The context window is a public good shared between:
- System prompt
- Conversation history
- Other Skills' metadata
- Your actual request
- Your skill content

**Default assumption**: the AI agent is already very smart. Only add context the AI agent doesn't already have.

Challenge each piece of information:
- "Does the AI agent really need this explanation?"
- "Can I assume the AI agent knows this?"
- "Does this paragraph justify its token cost?"

**Bad Example** (150 tokens):
```markdown
PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available...
```

**Good Example** (50 tokens):
```markdown
Use pdfplumber for text extraction:

\`\`\`python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
\`\`\`
```

### 2. Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability.

**High Freedom** (text-based instructions):
- Multiple approaches are valid
- Decisions depend on context
- Heuristics guide the approach

**Medium Freedom** (pseudocode or scripts with parameters):
- A preferred pattern exists
- Some variation is acceptable
- Configuration affects behavior

**Low Freedom** (specific scripts, few or no parameters):
- Operations are fragile and error-prone
- Consistency is critical
- A specific sequence must be followed

**Analogy**: Think of the AI agent navigating a path:
- **Narrow bridge with cliffs**: Only one safe way (low freedom) - provide exact instructions
- **Open field**: Many paths work (high freedom) - give general direction

### 3. Test with All Model Tiers

Skills work differently across model tiers. Test with all tiers you plan to use:
- **Fast models** (economical): Does the skill provide enough guidance?
- **Balanced models** (general use): Is the skill clear and efficient?
- **Powerful models** (advanced reasoning): Does the skill avoid over-explaining?

### 4. Progressive Disclosure

Keep SKILL.md body under 500 lines for optimal performance.

**What to Keep in SKILL.md**:
- YAML frontmatter
- Overview and quick start
- Workflow steps (high-level)
- Quick reference for common operations
- Links to detailed guides

**What to Move to Reference Files**:
- Detailed examples
- Comprehensive API documentation
- Extended explanations and rationale
- Domain-specific deep dives
- Historical context and old patterns
- Troubleshooting guides

**Reference Files**:
- Keep one level deep from SKILL.md (no nesting)
- Use descriptive names: `EXAMPLES.md`, `API_REFERENCE.md`
- The AI agent reads them only when needed (no context penalty until accessed)

### 5. Design for Composability

AI agents can load multiple skills simultaneously. Your skill should work well alongside others:

- **Don't assume exclusivity**: Other skills may be active at the same time
- **Use negative triggers**: Specify when NOT to use your skill (e.g., "Do NOT use for X, use Y skill instead")
- **Reference other skills**: When a task falls outside your scope, point to the right skill
- **Avoid conflicts**: Don't override general behaviors unless necessary

### 6. Portability

Skills work identically across any AI agent product (coding assistants, chat interfaces, API). Write skills with agent-agnostic language:

- Use "the AI agent" instead of product-specific names
- Don't assume specific IDE or product features
- Test across different environments when possible

### 7. Workflows and Feedback Loops

Break complex operations into clear, sequential steps. For quality-critical tasks, implement validation loops:

**Pattern**: Run validator → fix errors → repeat

**Example Workflow with Checklist**:
````markdown
## Document editing process

Copy this checklist and track progress:

\`\`\`
Task Progress:
- [ ] Step 1: Make edits to document.xml
- [ ] Step 2: Validate immediately
- [ ] Step 3: Fix issues if validation fails
- [ ] Step 4: Rebuild document
- [ ] Step 5: Test output
\`\`\`

**Step 2: Validate immediately**

\`\`\`bash
python scripts/validate.py unpacked_dir/
\`\`\`

If validation fails:
- Review error message carefully
- Fix issues in XML
- Run validation again

**Only proceed when validation passes.**
````

### 8. Iterate on a Single Task First

The most effective skill creators iterate on a single challenging task until the AI agent succeeds, then extract the winning approach into a skill. Don't try to handle every edge case upfront — perfect one scenario, then expand.

### 9. Evaluation-Driven Development

Create evaluations BEFORE writing extensive documentation.

**Process**:
1. **Identify gaps**: Run the AI agent on tasks without a Skill, document failures
2. **Create evaluations**: Build 3 scenarios that test these gaps
3. **Establish baseline**: Measure the AI agent's performance without the skill
4. **Write minimal instructions**: Create just enough to pass evaluations
5. **Iterate**: Execute evaluations, refine based on results

**Evaluation Structure**:
```json
{
  "skills": ["skill-name"],
  "query": "User request that triggers this skill",
  "files": ["test-files/input.txt"],
  "expected_behavior": [
    "First requirement to verify",
    "Second requirement to verify",
    "Third requirement to verify"
  ]
}
```

### 10. Iterative Development with the AI agent

Use the AI agent ("AI agent A") to help create skills that other instances ("AI agent B") will use:

1. **Complete task without a skill**: Work through problem, notice what context you repeatedly provide
2. **Identify reusable pattern**: What context would help similar future tasks?
3. **Ask the AI agent A to create a skill**: "Create a Skill that captures this pattern"
4. **Review for conciseness**: Remove unnecessary explanations
5. **Test with the AI agent B**: Use the skill on related tasks, observe behavior
6. **Iterate**: Bring observations back to the AI agent A for refinement

## Structure Guidelines

### YAML Frontmatter Requirements

Every SKILL.md must start with:

```yaml
---
name: skill-name
description: Description text here...
---
```

Both fields are required and validated according to rules above.

### Content Organization

**Recommended sections**:
1. Overview / Quick Start
2. Usage (command syntax, arguments)
3. Input Format (if applicable)
4. Task Workflow (step-by-step with checklist)
5. Implementation Guidelines
6. Examples
7. Notes

**Progressive Disclosure**:
- Main SKILL.md: Under 500 lines
- Reference files: Detailed content loaded on-demand
- One level deep: SKILL.md → reference/FILE.md (no deeper nesting)

## Common Patterns

### Template Pattern

Provide templates for consistent output format:

````markdown
## Report Structure

ALWAYS use this exact template structure:

\`\`\`markdown
# [Analysis Title]

## Executive Summary
[One-paragraph overview]

## Key Findings
- Finding 1 with supporting data
- Finding 2 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
\`\`\`
````

### Examples Pattern

For skills where output quality depends on examples:

````markdown
## Commit Message Format

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
\`\`\`
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
\`\`\`

**Example 2:**
Input: Fixed bug where dates displayed incorrectly
Output:
\`\`\`
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
\`\`\`
````

### Conditional Workflow Pattern

Guide the AI agent through decision points:

```markdown
## Document Modification Workflow

1. Determine the modification type:

   **Creating new content?** → Follow "Creation workflow"
   **Editing existing content?** → Follow "Editing workflow"

2. Creation workflow:
   - Use docx-js library
   - Build document from scratch
   - Export to .docx format

3. Editing workflow:
   - Unpack existing document
   - Modify XML directly
   - Validate after each change
   - Repack when complete
```

## Anti-Patterns to Avoid

### Don't Include README.md in Skill Folders

All documentation belongs in SKILL.md or reference/ files:
- ✓ Good: `SKILL.md`, `reference/GUIDE.md`
- ✗ Bad: `README.md` in skill root

**Why**: SKILL.md IS the documentation. A README.md creates confusion about which file is authoritative and wastes tokens.

### Don't Use Windows-Style Paths

Always use forward slashes, even on Windows:
- ✓ Good: `scripts/helper.py`, `reference/guide.md`
- ✗ Bad: `scripts\helper.py`, `reference\guide.md`

### Don't Offer Too Many Options

Provide a default with escape hatch:

````markdown
Good: Use pdfplumber for text extraction.

For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
````

Avoid: "You can use pypdf, or pdfplumber, or PyMuPDF, or pdf2image, or..."

### Don't Include Time-Sensitive Information

Bad: "If you're doing this before August 2025, use the old API..."

Good: Use an "Old Patterns" collapsible section:
````markdown
## Current Method

Use the v2 API endpoint: `api.example.com/v2/messages`

## Old Patterns

<details>
<summary>Legacy v1 API (deprecated 2025-08)</summary>

The v1 API used: `api.example.com/v1/messages`

This endpoint is no longer supported.
</details>
````

### Don't Assume Tools Are Installed

Bad: "Use the pdf library to process the file."

Good:
````markdown
Install required package:

\`\`\`bash
pip install pypdf
\`\`\`

Then use it:

\`\`\`python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
\`\`\`
````

## Skills with Executable Code

### Solve, Don't Punt

Handle error conditions in scripts rather than punting to the AI agent:

**Good Example**:
```python
def process_file(path):
    """Process file, creating if it doesn't exist."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, 'w') as f:
            f.write('')
        return ''
```

**Bad Example**:
```python
def process_file(path):
    # Just fail and let the AI agent figure it out
    return open(path).read()
```

### Provide Utility Scripts

Pre-made scripts are more reliable than generated code:

**Benefits**:
- More reliable than generated code
- Save tokens (no code in context)
- Save time (no generation required)
- Ensure consistency across uses

Scripts are executed via bash without loading their full contents into context. Only output consumes tokens.

### Create Verifiable Intermediate Outputs

For complex, open-ended tasks, use "plan-validate-execute" pattern:

1. The AI agent creates a plan file (structured format)
2. Script validates the plan
3. If valid, execute; if invalid, the AI agent fixes and re-validates
4. Final verification after execution

This catches errors early before they propagate.

## Technical Notes

- SKILL.md under 500 lines for optimal performance
- Use forward slashes in all file paths (cross-platform)
- No README.md in skill root folder — use SKILL.md and reference/ files
- Directory name must match the `name` field in frontmatter
- Static resources (templates, images, data files) go in `assets/` directory
- MCP tools: Use fully qualified names (`ServerName:tool_name`)
- Package dependencies: List required packages, verify availability
- Test with real usage scenarios, not just hypotheticals
- Skills work identically across any AI agent product

## Checklist for Effective Skills

Before sharing a Skill:

**Core Quality**:
- [ ] Description is specific and includes key terms
- [ ] Description includes both WHAT and WHEN
- [ ] SKILL.md body is under 500 lines
- [ ] No time-sensitive information
- [ ] Consistent terminology throughout
- [ ] Examples are concrete, not abstract
- [ ] File references are one level deep
- [ ] Progressive disclosure used appropriately
- [ ] No README.md in skill root folder
- [ ] Directory name matches `name` field
- [ ] Static resources in assets/ directory (if applicable)
- [ ] Description includes negative triggers (when NOT to use)
- [ ] Skill works well alongside other skills (composability)

**Code and Scripts** (if applicable):
- [ ] Scripts solve problems rather than punt to the AI agent
- [ ] Error handling is explicit and helpful
- [ ] Required packages listed and verified
- [ ] No Windows-style paths
- [ ] Validation/verification steps for critical operations

**Testing**:
- [ ] At least 3 evaluations created
- [ ] Tested across fast, balanced, and powerful model tiers
- [ ] Tested with real usage scenarios
- [ ] Team feedback incorporated (if applicable)
