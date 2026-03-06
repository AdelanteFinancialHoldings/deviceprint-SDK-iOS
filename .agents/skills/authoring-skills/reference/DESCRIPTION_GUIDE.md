# Skill Description Writing Guide

Detailed guidance on writing effective skill descriptions that follow best practices.

## Validation Rules (Required)

- **Maximum length**: 1024 characters
- **Required**: Cannot be empty
- **No XML tags**: Cannot contain `<`, `>`, `&`
- **Point of view**: MUST be in third person
- **Content**: Include WHAT and WHEN

## The "What + When" Pattern

Effective descriptions have two parts:

### Part 1: What (The Capability)
Clearly state what the skill does.

**Good examples**:
- "Extracts text and tables from PDF files"
- "Analyzes spreadsheet data and generates insights"
- "Manages database migration workflows with validation"
- "Tests API endpoints for correctness and performance"

### Part 2: When (The Triggers)
Specify when to use this skill with discovery keywords.

**Good examples**:
- "Use when working with PDF files or when the user mentions PDFs"
- "Use for spreadsheet analysis, data exploration, or Excel files"
- "Use when migrating databases or managing schema changes"
- "Use when testing APIs, endpoints, or HTTP services"

### Complete Examples (What + When)

**PDF Processing**:
```
Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**Spreadsheet Analysis**:
```
Analyzes Excel spreadsheets, creates pivot tables, generates charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.
```

**Database Migration**:
```
Manages database schema migrations with validation and rollback support. Use when migrating databases, updating schemas, or when the user mentions migrations or database changes.
```

## Negative Triggers (When NOT to Use)

Effective descriptions also specify when the skill should NOT be used. This prevents false activations and guides discovery.

### Why Negative Triggers Matter

Without negative triggers:
- Skill may activate for adjacent but unrelated tasks
- Users waste time with wrong skill activations
- Other more appropriate skills get bypassed

### Adding Negative Triggers

After the positive "Use when..." section, add a "Do NOT use..." clause:

**Pattern**:
```
[What + When]. Do NOT use for [alternative task] (use [other-skill] instead).
```

**Examples**:

```
Extracts text from PDF files. Use when working with PDFs or document extraction.
Do NOT use for simple text file operations (use standard file tools instead).
```

```
Manages database migrations with validation. Use when migrating databases or updating schemas.
Do NOT use for one-off SQL queries or data exploration (use querying-databases skill instead).
```

```
Analyzes spreadsheet data and generates insights. Use when working with Excel or CSV analysis.
Do NOT use for creating new spreadsheets from scratch (use generating-spreadsheets skill instead).
```

### Tips for Negative Triggers

- Identify the 1-2 most common false trigger scenarios
- Reference the correct skill or tool when possible
- Keep negative triggers concise — one sentence is usually enough
- Focus on adjacent tasks that share keywords with your skill

## Third Person Requirement

**Critical**: Descriptions are injected into the system prompt and MUST be in third person.

### Why Third Person?

Inconsistent point-of-view can cause discovery problems. The system prompt uses third person throughout, and your description must match.

### Bad Examples (First/Second Person)

- ✗ "I help you process PDF files" - First person ("I")
- ✗ "I can extract text from documents" - First person ("I")
- ✗ "You can use this to analyze data" - Second person ("you")
- ✗ "Use this skill when you need to..." - Second person ("you")
- ✗ "We help with database management" - First person plural ("we")
- ✗ "Our tool processes files" - First person possessive ("our")

### Good Examples (Third Person)

- ✓ "Processes PDF files and extracts text"
- ✓ "Extracts text from documents"
- ✓ "Analyzes data and generates insights"
- ✓ "Use when database management is needed"
- ✓ "Helps with database management"
- ✓ "Processes files automatically"

### POV Detection

The validation script checks for these indicators:
- "I" - First person singular
- "you", "your" - Second person
- "we", "our" - First person plural

**Even one instance fails validation**.

## Specificity: Key Terms for Discovery

Use specific, searchable terms that users might mention:

### Good (Specific Keywords)
```
Extracts text and tables from PDF files, fills forms, merges documents.
Use when working with PDFs, forms, document extraction, or Adobe files.
```

Keywords: PDF, forms, document extraction, Adobe
→ Discoverable when user mentions any of these

### Bad (Vague Terms)
```
Helps with documents and files.
```

Keywords: documents, files (too generic)
→ Not discoverable, matches too many things

### Keyword Strategy

**Include**:
- File formats: PDF, CSV, JSON, XML, Excel, XLSX
- Operations: extract, analyze, convert, validate, merge
- Domain terms: migration, endpoint, schema, deployment
- Tool names: Docker, Kubernetes, PostgreSQL, React
- Synonyms: spreadsheet/Excel, document/PDF, API/endpoint

**Example with good keywords**:
```
Analyzes CSV and Excel spreadsheets, creates pivot tables, generates visualizations.
Use when working with tabular data, .xlsx files, .csv files, Excel analysis, or data exploration.
```

Keywords: CSV, Excel, spreadsheets, pivot tables, visualizations, tabular data, .xlsx, data exploration

## Length Considerations

**Maximum**: 1024 characters (hard limit)
**Recommended**: 150-300 characters (sweet spot)
**Minimum**: At least 50 characters for adequate description

### Good Lengths

**Concise** (150 chars):
```
Processes PDF files and extracts text. Use when working with PDFs or document extraction.
```

**Detailed** (280 chars):
```
Extracts text and tables from PDF files, fills form fields, merges multiple documents, and converts between PDF and other formats. Use when working with PDF files, forms, document extraction, merging PDFs, or when the user mentions Adobe files or document processing.
```

**Comprehensive** (450 chars):
```
Analyzes BigQuery datasets across finance, sales, and product domains. Provides schema information, common query patterns, and data validation. Generates reports with visualizations and statistical analysis. Use when working with BigQuery, analyzing business data, querying sales metrics, financial reporting, product analytics, or when the user mentions Google Cloud data, SQL analysis, or data warehousing.
```

### Too Short (Not Enough Context)

```
Processes files.
```
- Missing: What files? What processing? When to use?

```
Helps with databases.
```
- Missing: What help? What operations? When to use?

### Too Long (Approaching Limit)

If approaching 1024 characters, you're including too much detail. The description should be a summary; detailed information belongs in SKILL.md.

**Trim by**:
- Removing redundant phrases
- Eliminating unnecessary adjectives
- Focusing on primary capabilities
- Moving examples to SKILL.md

## Anti-Patterns to Avoid

### Vague Descriptions

✗ "Helps with documents"
✗ "Processes data"
✗ "Does stuff with files"
✗ "Useful tool for tasks"

**Why they fail**: No specific information, not discoverable

### Feature Lists Without Context

✗ "Has features A, B, C, D, E, F, G..."

**Better**: Pick the top 2-3 features and include "when to use"

### Marketing Language

✗ "The ultimate solution for all your PDF needs"
✗ "Revolutionary approach to data analysis"
✗ "Best-in-class document processing"

**Why they fail**: Not informative, sounds like advertising

### Implementation Details

✗ "Uses pdfplumber library to parse PDF structure and extract text using OCR when needed"

**Why it fails**: Too technical, belongs in SKILL.md

**Better**: "Extracts text from PDF files including scanned documents"

### Historical Context

✗ "Originally created for Project X, now updated for Y"
✗ "Replaces the old PDF tool we had before"

**Why it fails**: History doesn't help discovery

## Domain-Specific Patterns

### Data Operations
```
Analyzes [data type], performs [operations], generates [outputs].
Use when working with [formats], [tools], or [use cases].
```

Example:
```
Analyzes CSV and JSON data, performs validation and transformation, generates cleaned datasets.
Use when working with data files, ETL pipelines, or data quality checks.
```

### Development Operations
```
[Action] [target], provides [capabilities], supports [features].
Use when [scenario] or when the user mentions [keywords].
```

Example:
```
Tests API endpoints, validates responses, checks performance benchmarks.
Use when testing APIs, validating services, or when the user mentions endpoint testing or HTTP validation.
```

### Document Operations
```
[Operations] for [document type], including [capabilities].
Use when working with [formats] or [tasks].
```

Example:
```
Generates financial reports from data sources, including charts and statistical analysis.
Use when creating reports, financial documentation, or business intelligence outputs.
```

## Handling Multi-Feature Skills

If your skill does many things:

### Option 1: Group by Theme
```
Manages complete database lifecycle including migrations, backups, and monitoring.
Use when working with databases, schema changes, or data management tasks.
```

### Option 2: List Top 3-4 Features
```
Processes PDF files: extracts text, fills forms, merges documents, converts formats.
Use when working with PDFs or document processing.
```

### Option 3: Focus on Primary + Mention Secondary
```
Primarily extracts data from various file formats (CSV, JSON, XML), also validates structure and converts between formats.
Use when working with structured data files or data transformation.
```

## Testing Your Description

Ask yourself:

1. **Third person?** No "I", "you", "we"?
2. **What is clear?** Can someone understand the capability?
3. **When is specified?** Are triggers/keywords included?
4. **Specific enough?** Not vague or generic?
5. **Discoverable?** Includes searchable keywords?
6. **Right length?** Not too short, not approaching 1024?

## Common Transformations

| Weak Description | Strong Description | What Changed |
|------------------|-------------------|--------------|
| "Helps with PDFs" | "Extracts text from PDF files. Use when working with PDFs or document extraction." | Added specific operation + when clause |
| "I process documents" | "Processes Word and PDF documents. Use for document conversion or text extraction." | Removed first person, added specifics |
| "Useful for data" | "Analyzes CSV and Excel data. Use when working with spreadsheets or tabular data." | Added specific data types + keywords |
| "You can use this for APIs" | "Tests API endpoints and validates responses. Use when testing REST APIs or HTTP services." | Removed second person, added operations |

## Real Examples Analysis

### Good Example 1: tracing-assets-to-binaries
```
Traces asset inventory (hosts and API paths) to their serving binaries through Kubernetes ingress and deployments. Use when analyzing infrastructure assets, mapping endpoints to executables, or documenting which binaries serve which inventory items.
```

**Why it's good**:
- ✓ Third person throughout
- ✓ Clear what: "traces asset inventory... to binaries"
- ✓ Clear when: "analyzing infrastructure", "mapping endpoints", "documenting binaries"
- ✓ Specific keywords: Kubernetes, ingress, deployments, infrastructure
- ✓ Good length: 261 characters

### Good Example 2: authoring-skills
```
Guides creation of new the AI agent skills following best practices. Use when creating a new skill, improving skill structure, validating skill metadata, or learning about skill authoring patterns. Includes self-improvement mechanism to learn from usage.
```

**Why it's good**:
- ✓ Third person
- ✓ Clear what: "guides creation of skills"
- ✓ Clear when: multiple use cases listed
- ✓ Specific keywords: skill creation, best practices, validation, authoring
- ✓ Bonus feature mentioned: self-improvement
- ✓ Good length: 274 characters

## Revision Checklist

Before finalizing your description:

- [ ] Maximum 1024 characters
- [ ] Third person only (no "I", "you", "we")
- [ ] Includes WHAT the skill does
- [ ] Includes WHEN to use it
- [ ] Contains specific, searchable keywords
- [ ] No XML characters (<, >, &)
- [ ] Not too vague or generic
- [ ] Not too technical (implementation details)
- [ ] Proper grammar and punctuation
- [ ] Tested with validate_description.py script
