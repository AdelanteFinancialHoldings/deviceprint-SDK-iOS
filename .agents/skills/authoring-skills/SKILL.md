---
name: authoring-skills
description: Guides creation of new AI Agent Skills following best practices and industry standards. Use when creating a new skill, building a skill, authoring a skill, setting up a new skill, improving skill structure, validating skill metadata, or learning about skill authoring patterns. Includes self-improvement mechanism to learn from usage.
---

# Authoring Skills

Create effective AI Agent Skills that follow industry best practices and the Agent Skills specification.

## Quick Start

When ready to create a Skill, use this workflow:

```
Skill Creation Progress:
- [ ] Step 1: Review best practices
- [ ] Step 2: Define use cases and requirements
- [ ] Step 3: Validate skill name
- [ ] Step 4: Craft description
- [ ] Step 5: Choose structure pattern
- [ ] Step 6: Create SKILL.md
- [ ] Step 7: Suggest progressive disclosure
- [ ] Step 8: Recommend evaluation creation
- [ ] Step 9: Collect feedback and self-improve
```

## Step 1: Review Best Practices

Read the bundled best practices reference:

[reference/BEST_PRACTICES.md](reference/BEST_PRACTICES.md)

**Key sections to review**:
- Validation Rules (name and description requirements)
- Core Principles (concise is key, progressive disclosure)
- Structure Guidelines (SKILL.md under 500 lines)
- Common Patterns (templates, examples, workflows)

## Step 2: Define Use Cases and Requirements

### Identify Skill Category

Before gathering requirements, identify which category fits:

1. **Document & Asset Creation** — Creating consistent output (documents, apps, designs, code). Key techniques: embedded style guides, template structures, quality checklists.
2. **Workflow Automation** — Multi-step processes with consistent methodology. Key techniques: step-by-step workflow with validation gates, iterative refinement loops.
3. **MCP Enhancement** — Workflow guidance to enhance MCP tool access. Key techniques: coordinates multiple MCP calls, embeds domain expertise.

The category guides which template to choose (Step 5) and which workflow patterns apply.

### Define Use Cases

Before writing any instructions, define 2-3 concrete use cases:

```
Use Case: [Name]
  Trigger: [What the user says or does]
  Steps:
    1. [First action]
    2. [Second action]
    3. [Third action]
  Result: [Expected outcome]
```

### Define Success Criteria

For each use case, define measurable success:

**Quantitative**:
- Triggers on 90%+ of relevant queries
- Completes workflow in under N tool calls
- Zero failed API/script calls for valid inputs

**Qualitative**:
- Users don't need to prompt about next steps
- Consistent results across sessions
- Works across fast, balanced, and powerful AI models

### Gather Requirements

Ask the user:
1. What task should this skill help with?
2. What context does the AI agent need repeatedly for this task?
3. Are there specific tools, scripts, or workflows involved?
4. Who will use this skill (just you, a team)?
5. Does this require executable scripts or is it text-only guidance?

Listen for:
- **Domain-specific terminology**: Will need to be in the skill
- **Workflow complexity**: Single-step vs multi-step processes
- **Need for executable scripts**: Validation, automation, data processing
- **Validation requirements**: Does output need to be checked?
- **Fragility**: How critical is consistency vs flexibility?

**Tip**: The answers guide which template to use (Step 5). See [reference/WORKFLOW_PATTERNS.md](reference/WORKFLOW_PATTERNS.md) for common patterns.

## How Validation Works (Steps 3-4)

**Two complementary tools for validation**:

### Validation Scripts (The Enforcer)
- **Purpose**: Immediate validation — "Is this valid?"
- **Output**: Pass/fail with specific errors
- **Usage**: Run during Steps 3 and 4 to catch errors early

### Reference Guides (The Teacher)
- **Purpose**: Deep guidance — "How do I write WELL?"
- **Content**: Examples, anti-patterns, best practices, transformations
- **Usage**: Read when you need deeper understanding or want to improve quality

**Pattern**:
1. Run script → Get immediate validation feedback
2. If confused or want to improve → Read reference guide for detailed examples

## Step 3: Validate Skill Name

**Script validates**, **guide teaches** — see [How Validation Works](#how-validation-works-steps-3-4) above.

Run validation script:
```bash
python scripts/validate_name.py "<proposed-name>"
```

**Validation Rules**:
- Maximum 64 characters
- Lowercase letters, numbers, hyphens only
- No start/end with hyphens; no consecutive hyphens (`--`)
- No XML tags (< > &)
- No reserved words ("anthropic", "claude")
- **Directory name must match the `name` field** in frontmatter

**Naming Pattern** (gerund form required):
- Good: `processing-pdfs`, `analyzing-spreadsheets`, `managing-databases`
- Rejected: `pdf-processing`, `spreadsheet-analysis` (not gerund form)
- Rejected: `--bad-name`, `bad--name`, `bad-name-` (invalid hyphens)
- Avoid: `helper`, `utils`, `tools` (too vague)

If validation fails:
- Script shows specific error and suggestions
- Iterate with user until valid name confirmed

For detailed guidance, see [NAMING_GUIDE](reference/NAMING_GUIDE.md)

## Step 4: Craft Description

**Script validates**, **guide teaches** — see [How Validation Works](#how-validation-works-steps-3-4) above.

Run validation script:
```bash
python scripts/validate_description.py "<proposed-description>"
```

**Validation Rules**:
- Maximum 1024 characters
- Non-empty (required)
- No XML tags
- Third person only (no "I", "you", "we", "your")
- Should include "when to use" guidance

**Content Requirements**:
- Write in third person
- Include WHAT the skill does
- Include WHEN to use it (positive triggers)
- Include WHEN NOT to use it (negative triggers)
- Use specific key terms for discoverability

**Good Example**:
```
Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction. Do NOT use for simple text file operations (use standard file tools instead).
```

**Negative Triggers** — help prevent false activations:
```
Do NOT use for [alternative task] (use [other-skill] instead).
```

If validation fails:
- Script shows specific errors and suggestions
- Iterate with user until valid description confirmed

For detailed guidance, see [DESCRIPTION_GUIDE](reference/DESCRIPTION_GUIDE.md)

## Step 5: Choose Structure Pattern

Select appropriate template based on complexity and category:

**Basic skill** (text instructions only):
- Template: [TEMPLATE_BASIC](assets/TEMPLATE_BASIC.md)
- For: Simple workflows, analysis tasks, document processes
- Category fit: Document & Asset Creation
- No executable scripts needed

**Skill with scripts**:
- Template: [TEMPLATE_WITH_SCRIPTS](assets/TEMPLATE_WITH_SCRIPTS.md)
- For: Tasks requiring validation, automation, or utilities
- Category fit: Workflow Automation
- Includes scripts/ directory

**Progressive disclosure**:
- Template: [TEMPLATE_PROGRESSIVE](assets/TEMPLATE_PROGRESSIVE.md)
- For: Complex skills approaching 500-line limit
- Category fit: MCP Enhancement, multi-domain analysis
- Splits content into reference files

Ask user which pattern fits their needs, or recommend based on Step 2 answers.

**Composability**: Skills can be loaded simultaneously. Design your skill to work well alongside others — don't assume it's the only capability available. Reference other skills when appropriate (e.g., "For X, use the Y skill instead").

See [PROGRESSIVE_DISCLOSURE](reference/PROGRESSIVE_DISCLOSURE.md) for detailed guidance on when to split. See [reference/WORKFLOW_PATTERNS.md](reference/WORKFLOW_PATTERNS.md) for common workflow patterns.

## Step 6: Create SKILL.md

Run structure creation script:
```bash
python scripts/create_skill_structure.py \
  --name "<skill-name>" \
  --description "<skill-description>" \
  --template "<basic|scripts|progressive>" \
  --output-dir ".agents/skills/<skill-name>"
```

This creates:
- Skill directory: `.agents/skills/<skill-name>/` (directory name matches `name` field)
- SKILL.md with validated YAML frontmatter
- Appropriate template content (includes self-improvement step)
- Subdirectories based on template (scripts/, reference/, etc.)
- **reference/IMPROVEMENTS.md** for Learning Mode self-improvement

### Optional YAML Fields

In addition to the required `name` and `description`, consider adding:

```yaml
---
name: your-skill-name
description: Your skill description...
compatibility: Designed for AI coding agents with Bash and file system access
allowed-tools: "Bash(python:*) Read Write Edit"
metadata:
  author: your-team-name
  mcp-server: server-name-if-applicable
---
```

- **compatibility** (1-500 chars): Environment requirements — intended product, required system packages, network access needs
- **allowed-tools**: Space-delimited list of pre-approved tools (experimental)
- **metadata**: Arbitrary key-value pairs — `author` and `mcp-server` recommended

### Important Rules

- **No README.md** in the skill root folder. All documentation goes in SKILL.md or reference/.
- **Directory name** must match the `name` field exactly.
- All static resources (templates, images, data files) go in `assets/` directory.
- Reference files go in `reference/` directory, one level deep only.

## Step 7: Suggest Progressive Disclosure

Check if SKILL.md body exceeds 400 lines (warning threshold):

If approaching 400-500 lines:
1. Identify separable sections (API references, domain content, advanced features, extensive examples)
2. Suggest reference file names
3. Keep high-level overview in SKILL.md, move details to reference/
4. Ensure references are one level deep (no nesting)

**Keep SKILL.md under 500 lines for optimal performance.**

If under 400 lines: mention threshold for future reference, no action needed now.

See [PROGRESSIVE_DISCLOSURE](reference/PROGRESSIVE_DISCLOSURE.md) for split patterns and examples.

## Step 8: Recommend Evaluation Creation

Suggest creating evaluations BEFORE extensive documentation:

**Evaluation-Driven Development**:
1. **Identify gaps**: What does the AI agent struggle with without this skill?
2. **Create 3 test scenarios**: Real-world use cases
3. **Establish baseline**: Measure the AI agent's performance without the skill
4. **Iterate on a single task first**: Perfect one challenging scenario before expanding
5. **Refine**: Add details only where gaps remain

### Trigger Testing

Create trigger test suites to verify skill discovery:

**Should trigger** (skill should activate):
- "Help me [primary use case]"
- "[Key term] for [scenario]"
- Natural variations of the use cases defined in Step 2

**Should NOT trigger** (skill should NOT activate):
- Requests for adjacent but different tasks
- Generic requests that could match too broadly
- Tasks better handled by other skills

**Example evaluation**:
```json
{
  "skills": ["your-skill-name"],
  "query": "User request that should trigger this skill",
  "expected_behavior": [
    "First requirement to verify",
    "Second requirement to verify"
  ]
}
```

For detailed guidance, see [EVALUATION_GUIDE](reference/EVALUATION_GUIDE.md)

## Step 9: Collect Feedback and Self-Improve

**CRITICAL STEP**: After skill creation, gather feedback to improve THIS skill (authoring-skills).

Ask the user:
1. "Did anything go wrong during skill creation?"
2. "What could be improved about this process?"
3. "Were any instructions unclear or missing?"
4. "Did the validation scripts work as expected?"
5. "Was the chosen template appropriate for your needs?"

### Learning Mode Self-Improvement

If issues or improvements are identified:

**Document the Feedback**:
```
- Issue description
- Context: When and how it occurred
- Which step was affected
- Proposed improvement
```

**Log Proposed Improvement** (DO NOT automatically apply changes):

Append to [IMPROVEMENTS](reference/IMPROVEMENTS.md):
```markdown
## [Date] - Proposed Improvement #N

**Issue**: [Description of what went wrong]
**Context**: [When and how it occurred]
**Affected Step**: Step X - [step name]

**Proposed Changes**:
- File: path/to/file
  - What should be changed
  - Why this would help

**Status**: PENDING MANUAL REVIEW

**Expected Result**: [What this would improve]
```

**Notify User**:
"I've logged a proposed improvement in IMPROVEMENTS.md. You can review and apply it manually when you're ready."

**If No Issues**: Still document: "Session completed successfully, no improvements needed."

### Manual Review and Application

Later, you can:
1. Read [reference/IMPROVEMENTS.md](reference/IMPROVEMENTS.md) to review proposals
2. Decide which improvements to apply
3. Ask the AI agent to implement specific approved improvements
4. Update IMPROVEMENTS.md with status (APPLIED or REJECTED with reason)

## Best Practices Summary

**Core Principles**:
1. **Concise is key**: Context window is a public good, only add what the AI agent doesn't know
2. **Set appropriate degrees of freedom**: Match specificity to task fragility
3. **Test with all model tiers**: Verify with fast, balanced, and powerful models
4. **Use progressive disclosure**: Keep SKILL.md under 500 lines, reference other files
5. **Build evaluations first**: Create tests before extensive documentation
6. **Iterate on a single task**: Perfect one scenario before expanding
7. **Design for composability**: Skills may run alongside others

**Structure Guidelines**:
- SKILL.md body under 500 lines (warning at 400)
- References one level deep from SKILL.md
- No README.md files in skill root folders
- Static resources in assets/ directory
- Directory name matches `name` field

For complete best practices, see [BEST_PRACTICES](reference/BEST_PRACTICES.md)

For validation script reference, see [VALIDATION_SCRIPTS](reference/VALIDATION_SCRIPTS.md)

For examples, see [EXAMPLES](reference/EXAMPLES.md)

## Notes

- Skills work identically across any AI agent product (coding assistants, chat interfaces, API)
- Always use forward slashes in paths (cross-platform)
- Validate early and often (fail fast)
- Use TodoWrite to track 9-step progress
- Step 9 is MANDATORY, not optional (Learning Mode)
- Log all feedback for transparency
- Test with real usage, not just hypotheticals
- Iterate based on observations, not assumptions

**File Organization Pattern**:
- Root: SKILL.md only (no README.md)
- Reference docs: reference/ directory
- Scripts: scripts/ directory
- Static resources: assets/ directory
- This keeps the root clean and applies progressive disclosure consistently

## Checking for Pending Improvements

When the skill is invoked, check for pending improvements:

```bash
grep "PENDING MANUAL REVIEW" reference/IMPROVEMENTS.md | wc -l
```

If count > 0, inform user:
"There are [N] pending improvement proposals in reference/IMPROVEMENTS.md. Would you like to review them before creating a new skill?"
