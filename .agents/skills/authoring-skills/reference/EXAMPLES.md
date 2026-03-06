# Skill Authoring Examples

Concrete examples of creating skills using the authoring-skills workflow.

## Example 1: Creating a Basic Skill

```
User: "I want to create a skill for analyzing JSON schemas"
Assistant:
1. Reviews best practices (Step 1)
2. Asks about requirements (Step 2)
3. Suggests name: "analyzing-json-schemas" (Step 3)
4. Validates name: ✓ Pass
5. Helps craft description (Step 4)
6. Validates description: ✓ Pass
7. Recommends: basic template (Step 5)
8. Creates skill structure (Step 6)
9. Checks line count: 150 lines, under threshold (Step 7)
10. Suggests creating 3 evaluations (Step 8)
11. Asks for feedback, logs any improvements (Step 9)
```

## Example 2: Creating a Skill with Scripts

```
User: "I need a skill for database migrations with validation"
Assistant:
1. Reviews best practices (Step 1)
2. Identifies need for validation scripts (Step 2)
3. Suggests name: "managing-database-migrations" (Step 3)
4. Validates successfully (Step 3-4)
5. Recommends: scripts template (Step 5)
6. Creates structure with scripts/ directory (Step 6)
7. Suggests validation scripts to bundle (Step 6)
8. Under 500 lines, no split needed (Step 7)
9. Recommends evaluations for migration scenarios (Step 8)
10. Collects feedback (Step 9)
```

## Example 3: Self-Improvement Scenario

```
User: "The description validation didn't catch that I was using first person"
Assistant:
1. Documents issue in reference/IMPROVEMENTS.md:
   - Issue: POV detection failed
   - Context: Description started with "I help..."
   - Proposed: Update validate_description.py to check for POV
   - Status: PENDING MANUAL REVIEW
2. Notifies user about logged improvement
3. User can later review and apply the fix
```

## Example 4: Use-Case Driven Skill

```
User: "I want a skill for sprint planning with Linear"

Use Case Definition:
  Use Case: Sprint Planning
  Trigger: User says "help me plan this sprint" or "create sprint tasks"
  Steps:
    1. Fetch current project status from Linear (via MCP)
    2. Analyze team velocity and capacity
    3. Suggest task prioritization
    4. Create tasks in Linear with proper labels and estimates
  Result: Fully planned sprint with tasks created

Success Criteria:
  Quantitative:
    - Triggers on 90% of sprint-related queries
    - Completes workflow in under 10 tool calls
  Qualitative:
    - Users don't need to prompt about next steps
    - Consistent results across sessions
```
