# Workflow Patterns for Skills

Common patterns for structuring skill workflows, adapted from industry best practices.

## Choosing Your Approach: Problem-First vs. Tool-First

- **Problem-first**: "I need to set up a project workspace" — The skill orchestrates the right calls in the right sequence. Users describe outcomes; the skill handles the tools.
- **Tool-first**: "I have an MCP server connected" — The skill teaches the AI agent the optimal workflows and best practices. Users have access; the skill provides expertise.

Most skills lean one direction. Knowing which framing fits helps you choose the right pattern below.

## Skill Categories

Before choosing a pattern, identify which category your skill falls into:

### Category 1: Document & Asset Creation
- **Used for**: Creating consistent, high-quality output (documents, presentations, apps, designs, code)
- **Key techniques**: Embedded style guides, template structures, quality checklists
- **Example**: A skill that creates production-grade frontend interfaces with consistent design quality

### Category 2: Workflow Automation
- **Used for**: Multi-step processes that benefit from consistent methodology
- **Key techniques**: Step-by-step workflow with validation gates, templates, iterative refinement loops
- **Example**: A skill that guides users through creating new skills with validation at each step

### Category 3: MCP Enhancement
- **Used for**: Workflow guidance to enhance the tool access an MCP server provides
- **Key techniques**: Coordinates multiple MCP calls, embeds domain expertise, provides context users would otherwise need to specify
- **Example**: A skill that analyzes and fixes bugs using error monitoring data via MCP

## Pattern 1: Sequential Workflow Orchestration

**Use when**: Users need multi-step processes in a specific order.

```markdown
## Workflow: Onboard New Customer

### Step 1: Create Account
Call MCP tool: `create_customer`
Parameters: name, email, company

### Step 2: Setup Payment
Call MCP tool: `setup_payment_method`
Wait for: payment method verification

### Step 3: Create Subscription
Call MCP tool: `create_subscription`
Parameters: plan_id, customer_id (from Step 1)

### Step 4: Send Welcome Email
Call MCP tool: `send_email`
Template: welcome_email_template
```

**Key techniques**:
- Explicit step ordering
- Dependencies between steps
- Validation at each stage
- Rollback instructions for failures

## Pattern 2: Multi-MCP Coordination

**Use when**: Workflows span multiple services.

```markdown
### Phase 1: Design Export (Figma MCP)
1. Export design assets
2. Generate design specifications
3. Create asset manifest

### Phase 2: Asset Storage (Drive MCP)
1. Create project folder
2. Upload all assets
3. Generate shareable links

### Phase 3: Task Creation (Linear MCP)
1. Create development tasks
2. Attach asset links to tasks
3. Assign to engineering team
```

**Key techniques**:
- Clear phase separation
- Data passing between MCPs
- Validation before moving to next phase
- Centralized error handling

## Pattern 3: Iterative Refinement

**Use when**: Output quality improves with iteration.

```markdown
## Iterative Report Creation

### Initial Draft
1. Fetch data via MCP
2. Generate first draft report
3. Save to temporary file

### Quality Check
1. Run validation script: `scripts/check_report.py`
2. Identify issues

### Refinement Loop
1. Address each identified issue
2. Regenerate affected sections
3. Re-validate
4. Repeat until quality threshold met

### Finalization
1. Apply final formatting
2. Generate summary
3. Save final version
```

**Key techniques**:
- Explicit quality criteria
- Iterative improvement
- Validation scripts
- Know when to stop iterating

## Pattern 4: Context-Aware Tool Selection

**Use when**: Same outcome, different tools depending on context.

```markdown
## Smart File Storage

### Decision Tree
1. Check file type and size
2. Determine best storage location:
   - Large files (>10MB): Use cloud storage MCP
   - Collaborative docs: Use Docs MCP
   - Code files: Use GitHub MCP
   - Temporary files: Use local storage

### Execute Storage
Based on decision:
- Call appropriate MCP tool
- Apply service-specific metadata
- Generate access link

### Provide Context to User
Explain why that storage was chosen
```

**Key techniques**:
- Clear decision criteria
- Fallback options
- Transparency about choices

## Pattern 5: Domain-Specific Intelligence

**Use when**: The skill adds specialized knowledge beyond tool access.

```markdown
## Payment Processing with Compliance

### Before Processing (Compliance Check)
1. Fetch transaction details via MCP
2. Apply compliance rules:
   - Check sanctions lists
   - Verify jurisdiction allowances
   - Assess risk level
3. Document compliance decision

### Processing
IF compliance passed:
    - Call payment processing MCP tool
    - Apply appropriate fraud checks
    - Process transaction
ELSE:
    - Flag for review
    - Create compliance case

### Audit Trail
- Log all compliance checks
- Record processing decisions
- Generate audit report
```

**Key techniques**:
- Domain expertise embedded in logic
- Compliance before action
- Comprehensive documentation
- Clear governance

## Choosing the Right Pattern

| Scenario | Recommended Pattern |
|----------|-------------------|
| Multi-step process in fixed order | Sequential Workflow |
| Workflow spanning multiple services | Multi-MCP Coordination |
| Quality-dependent output | Iterative Refinement |
| Context-dependent tool choice | Context-Aware Selection |
| Specialized domain knowledge needed | Domain-Specific Intelligence |
| Combination of the above | Compose multiple patterns |
