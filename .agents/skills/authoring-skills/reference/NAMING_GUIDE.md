# Skill Naming Guide

Detailed guidance on choosing effective skill names that follow best practices.

## Validation Rules (Required)

- **Maximum length**: 64 characters
- **Allowed characters**: Lowercase letters (a-z), numbers (0-9), hyphens (-) only
- **No start/end hyphens**: Must not start or end with `-`
- **No consecutive hyphens**: Must not contain `--`
- **No XML tags**: Cannot contain `<`, `>`, `&`
- **No reserved words**: Cannot contain "anthropic" or "claude"
- **Not empty**: Name is required
- **Directory match**: The skill directory name must match the `name` field exactly

## Required Naming Pattern: Gerund Form

**Gerund form** (verb + -ing) clearly describes the activity or capability:

### Good Examples (Gerund Form)
- `processing-pdfs` - Processing PDF files
- `analyzing-spreadsheets` - Analyzing spreadsheet data
- `managing-databases` - Managing database operations
- `testing-code` - Testing code quality
- `writing-documentation` - Writing documentation
- `generating-reports` - Generating report files
- `validating-data` - Validating data integrity
- `converting-formats` - Converting between formats
- `monitoring-systems` - Monitoring system health
- `deploying-applications` - Deploying applications

### Why Gerund Form Works

1. **Active voice**: Describes what the skill is doing
2. **Clear purpose**: Immediately understand the capability
3. **Consistent pattern**: Easy to predict and remember
4. **Searchable**: Natural language for discovery

## Anti-Patterns: Names to Avoid

### Too Vague
- ✗ `helper` - Helps with what?
- ✗ `utils` - What utilities?
- ✗ `tools` - What tools?
- ✗ `assistant` - Assists with what?
- ✗ `manager` - Manages what?

**Why these fail**: Not discoverable, no context about purpose

### Too Generic
- ✗ `documents` - Which documents? What operations?
- ✗ `data` - What kind of data? What does it do?
- ✗ `files` - Which files? What operations?
- ✗ `api` - Which API? What functionality?

**Why these fail**: Not specific enough, many possible meanings

### Wrong Tense/Form
- ✗ `process-pdfs` - Imperative (command form)
- ✗ `processes-pdfs` - Third person singular (awkward)
- ✗ `processed-pdfs` - Past tense (implies finished action)
- ✗ `pdf-processor` - Agent noun (less clear than gerund)
- ✗ `pdf-processing` - Noun phrase (not gerund form)
- ✗ `spreadsheet-analysis` - Noun phrase (not gerund form)
- ✗ `database-management` - Noun phrase (not gerund form)

**Use**: `processing-pdfs` ✓ (gerund form, present continuous)

### Inconsistent Patterns
Within your skill collection, be consistent:

**Bad** (inconsistent):
- `processing-pdfs`
- `spreadsheet-analyzer`
- `manage-databases`
- `code-test-util`

**Good** (consistent gerund):
- `processing-pdfs`
- `analyzing-spreadsheets`
- `managing-databases`
- `testing-code`

## Special Cases

### Numbers in Names

Numbers are allowed but use sparingly:

- ✓ `processing-pdfs-v2` - If you have versions
- ✓ `analyzing-data-v3` - Version indicators
- ✓ `migrating-from-v1-to-v2` - Specific migration skill

Avoid numbers that don't add meaning:
- ✗ `processing-pdfs-1` - Why 1?
- ✗ `tool-v42` - Arbitrary versioning

### Abbreviations

Use common abbreviations if widely recognized:

- ✓ `processing-pdfs` - PDF is universally known
- ✓ `analyzing-csv-files` - CSV is standard
- ✓ `managing-sql-databases` - SQL is common
- ✓ `working-with-json` - JSON is standard

Avoid obscure abbreviations:
- ✗ `processing-ptd-files` - What's PTD?
- ✗ `managing-xrf-data` - Not widely known

### Compound Operations

For skills that do multiple things, choose the primary operation:

**Good**:
- `processing-pdfs` - Even if it also validates and converts
- `analyzing-spreadsheets` - Even if it also formats and exports

**Acceptable** (if truly equal operations):
- `converting-and-validating-files` - Two equal operations
- `parsing-and-transforming-data` - Both are primary

**Avoid** (too many operations):
- ✗ `reading-parsing-validating-converting-exporting-data` - Too long, pick primary

## Length Considerations

**Maximum**: 64 characters (hard limit)
**Recommended**: 20-40 characters (sweet spot)

### Good Lengths
- `processing-pdfs` (15 chars) ✓
- `analyzing-spreadsheets` (23 chars) ✓
- `managing-database-migrations` (30 chars) ✓
- `generating-financial-reports` (31 chars) ✓

### Too Short (Not Descriptive)
- `pdf` (3 chars) - What about PDFs?
- `data` (4 chars) - Too vague

### Getting Long (But OK)
- `processing-and-validating-xml-documents` (42 chars) - Descriptive but long
- `analyzing-financial-spreadsheet-data` (38 chars) - Consider shortening

### Too Long (Approaching Limit)
- `managing-complex-database-migration-workflows-with-validation` (63 chars) - At limit
- Consider: `managing-database-migrations` instead

## Domain-Specific Patterns

### Data Operations
- `analyzing-[data-type]`: analyzing-sales-data, analyzing-logs
- `processing-[format]`: processing-json, processing-xml
- `converting-[format]`: converting-csv-to-json
- `validating-[type]`: validating-schemas, validating-credentials

### Development Operations
- `testing-[aspect]`: testing-api-endpoints, testing-performance
- `deploying-[target]`: deploying-containers, deploying-lambdas
- `building-[artifact]`: building-docker-images, building-packages
- `linting-[language]`: linting-python, linting-typescript

### Document Operations
- `generating-[doc-type]`: generating-reports, generating-invoices
- `formatting-[doc-type]`: formatting-markdown, formatting-latex
- `reviewing-[doc-type]`: reviewing-pull-requests, reviewing-designs

### System Operations
- `monitoring-[system]`: monitoring-services, monitoring-databases
- `managing-[resource]`: managing-containers, managing-secrets
- `configuring-[component]`: configuring-clusters, configuring-networks

## Quick Reference Table

| Pattern | Example | When to Use |
|---------|---------|-------------|
| Gerund form | `processing-pdfs` | Required for all skills |
| With version | `processing-pdfs-v2` | Multiple versions exist |
| Compound | `converting-and-validating` | Two equal operations |
| Domain-specific | `analyzing-sales-data` | Domain context important |

## Testing Your Name

Ask yourself:

1. **Does it start with a gerund?** The first word must end in "-ing" (e.g., `processing-`, `analyzing-`)
2. **Is it discoverable?** Would someone searching for this functionality find it?
3. **Is it specific?** Does it clearly indicate what it does?
4. **Is it consistent?** Does it match patterns in your other skills?
5. **Is it pronounceable?** Can you say it naturally?
6. **Is it future-proof?** Will it still make sense in a year?

## Common Transformations

If you have a vague name, transform it:

| Vague Name | Better Name | Transformation |
|------------|-------------|----------------|
| `helper` | `processing-pdfs` | Add specific action + object |
| `utils` | `validating-data` | Identify primary utility |
| `documents` | `generating-reports` | Add action verb |
| `api-tool` | `testing-api-endpoints` | Specify operation |
| `manager` | `managing-databases` | Add specific resource |

## Examples from Real Skills

**Good skill names** (gerund form):
- `tracing-assets-to-binaries` - Clear gerund form, specific operation
- `authoring-skills` - Gerund form, describes creation activity

**Names that need improvement** (not gerund form):
- ✗ `keybindings-help` → `configuring-keybindings` (gerund form)
- ✗ `asset-tracer` → `tracing-assets-to-binaries` (gerund form, more descriptive)
- ✗ `skill-helper` → `authoring-skills` (gerund form, clearer purpose)
