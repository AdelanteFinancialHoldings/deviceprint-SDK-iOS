# Evaluation Guide for Skills

How to create evaluations before extensive documentation (evaluation-driven development).

## What Are Evaluations?

**Evaluations** are test scenarios that verify your skill works as intended. They measure:
- Does the AI agent discover and use the skill?
- Does the AI agent follow the instructions correctly?
- Does the output meet requirements?

## Why Create Evaluations First?

### The Traditional Approach (Less Effective)
1. Write extensive documentation
2. Hope it covers everything
3. Test with real usage
4. Discover gaps
5. Add more documentation
6. Repeat

**Problem**: Over-documentation, unclear what actually helps

### Evaluation-Driven Approach (Better)
1. **Identify gaps**: What does the AI agent struggle with NOW?
2. **Create evaluations**: 3 test scenarios for those gaps
3. **Establish baseline**: Measure without the skill
4. **Write minimal instructions**: Just enough to pass evaluations
5. **Iterate**: Run evaluations, refine instructions

**Benefits**:
- Ensures skill solves real problems
- Prevents over-documentation
- Provides objective quality measure
- Guides iterative refinement

## Evaluation Structure

```json
{
  "skills": ["skill-name"],
  "query": "User request that should trigger this skill",
  "files": ["test-files/input.txt"],
  "expected_behavior": [
    "First requirement to verify",
    "Second requirement to verify",
    "Third requirement to verify"
  ]
}
```

### Fields Explained

**skills**: Array of skill names to load
- Use your skill name exactly as in YAML frontmatter
- Can include multiple skills if needed

**query**: The user request
- Write it as a user would ask
- Include natural language
- Mention key terms that should trigger discovery

**files**: Test input files (optional)
- Paths to any files needed for the test
- Relative to evaluation directory
- Can be empty array if no files needed

**expected_behavior**: Success criteria
- 3-5 specific, verifiable requirements
- What the AI agent should do, not how
- Observable outcomes, not internal state

## Creating Effective Evaluations

### Step 1: Identify Gaps

Before creating a skill, observe the AI agent without it:

**Try real tasks and note**:
- What information does the AI agent lack?
- What does the AI agent do incorrectly?
- What context do you repeatedly provide?
- Where does the AI agent make mistakes?

**Example gaps**:
- "The AI agent doesn't know the table schemas"
- "The AI agent forgets to validate before processing"
- "The AI agent uses wrong API endpoint format"
- "The AI agent doesn't follow Kubernetes precedence rules"

### Step 2: Create 3 Test Scenarios

**Scenario 1: Basic Happy Path**
- Simple, common use case
- Should work if basic instructions are followed
- Tests skill discovery and basic flow

**Scenario 2: Common Complexity**
- Real-world scenario with some complexity
- Tests that instructions handle typical cases
- May involve multiple steps or decisions

**Scenario 3: Edge Case or Error Handling**
- Less common but important case
- Tests that skill handles errors gracefully
- May test validation or boundary conditions

### Step 3: Write Clear Expected Behaviors

**Good** (specific, verifiable):
- "Creates a file named output.txt with extracted text"
- "Validates input before processing and shows specific error for missing field"
- "Uses Exact match precedence over Prefix match"

**Bad** (vague, not verifiable):
- "Processes the file correctly"
- "Handles errors well"
- "Follows best practices"

## Trigger Testing

Trigger testing verifies that your skill activates for the right queries and does NOT activate for the wrong ones. This is distinct from functional testing (which verifies the skill works correctly once activated).

### Should-Trigger Tests

Create test cases for queries that SHOULD activate your skill:

```json
{
  "type": "should_trigger",
  "query": "Help me extract text from this PDF",
  "expected_skill": "processing-pdfs",
  "notes": "Direct mention of PDF + extraction"
}
```

**Cover these variations**:
- Direct requests using primary keywords
- Indirect requests using synonyms or related terms
- Natural language variations ("help me with...", "I need to...", "can you...")
- Trigger phrases defined in your use cases (Step 2)

### Should-NOT-Trigger Tests

Create test cases for queries that should NOT activate your skill:

```json
{
  "type": "should_not_trigger",
  "query": "Read the contents of config.txt",
  "expected_skill": "none (or different skill)",
  "notes": "Simple text file - not a PDF task"
}
```

**Cover these scenarios**:
- Adjacent tasks that share keywords (e.g., "document" for both PDF and Word skills)
- Generic requests that could match too broadly
- Tasks better handled by other specific skills
- Edge cases where keywords appear in non-relevant context

### Trigger Test Suite Template

```json
[
  {"type": "should_trigger", "query": "...", "expected": "your-skill"},
  {"type": "should_trigger", "query": "...", "expected": "your-skill"},
  {"type": "should_trigger", "query": "...", "expected": "your-skill"},
  {"type": "should_not_trigger", "query": "...", "expected": "other"},
  {"type": "should_not_trigger", "query": "...", "expected": "none"}
]
```

**Goal**: 90%+ trigger accuracy — the skill activates for 90% of relevant queries and does not falsely activate for irrelevant ones.

## Example Evaluations

### Example 1: PDF Processing Skill

**Scenario 1: Basic extraction**
```json
{
  "skills": ["processing-pdfs"],
  "query": "Extract all text from document.pdf and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF file using an appropriate PDF processing library or command-line tool",
    "Extracts text content from all pages in the document without missing any pages",
    "Saves the extracted text to a file named output.txt in a clear, readable format"
  ]
}
```

**Scenario 2: Form filling**
```json
{
  "skills": ["processing-pdfs"],
  "query": "Fill the form fields in application.pdf with data from fields.json and save as completed.pdf",
  "files": ["test-files/application.pdf", "test-files/fields.json"],
  "expected_behavior": [
    "Analyzes the form structure in application.pdf to identify fillable fields",
    "Maps data from fields.json to corresponding form fields correctly",
    "Saves the completed form as completed.pdf with all fields filled",
    "Verifies the output file can be opened and contains the filled data"
  ]
}
```

**Scenario 3: Error handling**
```json
{
  "skills": ["processing-pdfs"],
  "query": "Extract text from missing-file.pdf",
  "files": [],
  "expected_behavior": [
    "Detects that the file does not exist",
    "Provides a clear error message indicating the file was not found",
    "Does not attempt to process or create empty output files",
    "Suggests checking the file path or providing a valid PDF file"
  ]
}
```

### Example 2: Database Migration Skill

**Scenario 1: Valid migration**
```json
{
  "skills": ["managing-database-migrations"],
  "query": "Apply the migration in migration_001.sql to the database",
  "files": ["test-files/migration_001.sql"],
  "expected_behavior": [
    "Validates the migration file syntax before attempting to apply it",
    "Creates a backup or documents the current schema state",
    "Applies the migration and confirms successful execution",
    "Logs the migration application with timestamp and migration ID"
  ]
}
```

**Scenario 2: Invalid migration**
```json
{
  "skills": ["managing-database-migrations"],
  "query": "Apply the migration in invalid_migration.sql",
  "files": ["test-files/invalid_migration.sql"],
  "expected_behavior": [
    "Validates the migration file and detects syntax errors",
    "Provides specific error messages about what is invalid",
    "Does not apply the invalid migration to the database",
    "Suggests how to fix the migration syntax"
  ]
}
```

**Scenario 3: Rollback**
```json
{
  "skills": ["managing-database-migrations"],
  "query": "Rollback the last migration",
  "files": [],
  "expected_behavior": [
    "Identifies the most recently applied migration",
    "Executes the rollback procedure for that migration",
    "Verifies the database schema has been reverted correctly",
    "Updates migration history to reflect the rollback"
  ]
}
```

### Example 3: Asset Tracing Skill

**Scenario 1: Single asset**
```json
{
  "skills": ["tracing-assets-to-binaries"],
  "query": "Trace the assets in backend_inventory.md to their binaries in the production/co environment",
  "files": ["backend_inventory.md"],
  "expected_behavior": [
    "Parses the inventory file and extracts all hosts and paths",
    "Finds ingress routing configurations for each host",
    "Maps paths to services using Kubernetes precedence rules (Exact before Prefix)",
    "Identifies the binaries from deployment files",
    "Generates asset-to-binary mapping files with correct naming format"
  ]
}
```

## Running Evaluations

Currently, there's no built-in evaluation runner. You must:

### Manual Evaluation Process

1. **Start fresh conversation**: New AI agent instance
2. **Load skill**: Ensure skill is available
3. **Provide test files**: Make files available
4. **Submit query**: Use exact query from evaluation
5. **Observe behavior**: Check each expected behavior
6. **Record results**: Pass/fail for each requirement

### Evaluation Scorecard

For each evaluation, track:

```
Evaluation: [Name/ID]
Skill: [skill-name]

Expected Behaviors:
- [ ] Behavior 1: [pass/fail with notes]
- [ ] Behavior 2: [pass/fail with notes]
- [ ] Behavior 3: [pass/fail with notes]

Overall: [X/3] requirements met

Notes:
- [What worked well]
- [What needs improvement]
- [Specific gaps to address]
```

## Iterating Based on Evaluations

### If Evaluation Fails

1. **Analyze failure**:
   - Which requirement failed?
   - Why did the AI agent not meet it?
   - Is information missing?
   - Are instructions unclear?

2. **Make minimal fix**:
   - Add specific missing information
   - Clarify ambiguous instruction
   - Add example if pattern unclear

3. **Re-run evaluation**:
   - Test with fresh instance
   - Verify fix addresses the issue
   - Ensure no regression on other requirements

4. **Repeat until pass**

### Baseline Comparison

Track improvement over iterations:

```
Evaluation Results:

Baseline (no skill):     0/3 requirements met
Iteration 1 (minimal):   1/3 requirements met
Iteration 2 (refined):   2/3 requirements met
Iteration 3 (final):     3/3 requirements met
```

**Goal**: Reach 3/3 with minimal, focused instructions

## Creating Test Files

Evaluations need test files. Create:

**test-files/ directory**:
```
test-files/
├── document.pdf           # Valid PDF for testing
├── application.pdf        # PDF form for testing
├── fields.json           # Test data
├── migration_001.sql     # Valid migration
├── invalid_migration.sql # Invalid for error testing
└── README.md             # Documents what each file tests
```

**Test file characteristics**:
- **Realistic**: Use real-world-like data
- **Minimal**: Small enough to process quickly
- **Diverse**: Cover different scenarios
- **Documented**: README explains purpose

## How Many Evaluations?

**Minimum**: 3 evaluations
- Basic happy path
- Common complexity
- Edge case / error handling

**Typical**: 3-5 evaluations
- Covers main use cases
- Tests key error scenarios
- Validates critical requirements

**Comprehensive**: 5-10 evaluations
- Multiple variations
- Many edge cases
- Complex scenarios

**Don't overdo it**: More than 10 evaluations suggests:
- Skill does too many things (consider splitting)
- Over-testing minor variations
- Diminishing returns

## Evaluation-Driven Development Flow

```
1. Identify gaps (observe the AI agent without skill)
   ↓
2. Create 3 evaluations (test scenarios)
   ↓
3. Establish baseline (run without skill) → 0/3 pass
   ↓
4. Write minimal SKILL.md (basic instructions)
   ↓
5. Run evaluations → 1/3 pass
   ↓
6. Refine instructions (address failures)
   ↓
7. Run evaluations → 2/3 pass
   ↓
8. Refine more (focus on last failure)
   ↓
9. Run evaluations → 3/3 pass ✓
   ↓
10. Skill is ready (not over-documented)
```

## Benefits of This Approach

**Prevents Over-Documentation**:
- Only add what's needed to pass evaluations
- No speculative documentation
- Focus on actual gaps

**Objective Quality Measure**:
- Pass/fail is clear
- Track improvement numerically
- Know when "good enough"

**Guides Prioritization**:
- Work on highest-value additions
- See impact of each change
- Avoid bikeshedding

**Builds Confidence**:
- Repeatable tests
- Regression detection
- Documented requirements

## Common Pitfalls

**Pitfall 1: Writing evaluations after documentation**
- **Problem**: Evaluations will pass by design
- **Solution**: Write evaluations first

**Pitfall 2: Vague expected behaviors**
- **Problem**: Can't objectively verify
- **Solution**: Make requirements specific and observable

**Pitfall 3: Too many evaluations**
- **Problem**: Diminishing returns, maintenance burden
- **Solution**: Start with 3, add only if needed

**Pitfall 4: Not running evaluations fresh**
- **Problem**: Conversation history affects results
- **Solution**: Always use fresh the AI agent instance

**Pitfall 5: Evaluations that test the AI agent, not skill**
- **Problem**: Testing general capabilities, not skill content
- **Solution**: Evaluations should fail without the skill

## Summary

**Evaluation-driven development ensures**:
- Skills solve real problems
- Documentation is minimal and focused
- Quality is objectively measurable
- Iterations are guided by data

**Process**:
1. Create 3 evaluations first
2. Establish baseline (without skill)
3. Write minimal instructions
4. Iterate based on evaluation results
5. Stop when evaluations pass consistently

**Result**: Concise, effective skills that solve real problems without over-documentation.
