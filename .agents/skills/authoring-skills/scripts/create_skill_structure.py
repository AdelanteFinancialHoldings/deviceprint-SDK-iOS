#!/usr/bin/env python3
"""Create skill directory structure with validated inputs.

Usage:
    python create_skill_structure.py \\
        --name "skill-name" \\
        --description "Description..." \\
        --template "basic" \\
        --output-dir ".agents/skills/skill-name"

Exit codes:
    0: Success
    1: Validation failure or error
"""

import argparse
import sys
from pathlib import Path
import shutil

# Import validation functions
try:
    from validate_name import validate_name
    from validate_description import validate_description
except ImportError:
    print("Error: Could not import validation functions")
    print("Ensure validate_name.py and validate_description.py are in the same directory")
    sys.exit(1)


AVAILABLE_TEMPLATES = ['basic', 'scripts', 'progressive']


def create_skill_structure(
    name: str,
    description: str,
    template: str,
    output_dir: str
) -> tuple[bool, list[str]]:
    """Create skill directory structure.

    Args:
        name: Validated skill name
        description: Validated skill description
        template: Template type (basic, scripts, progressive)
        output_dir: Output directory path

    Returns:
        Tuple of (success, messages)
    """
    messages = []
    output_path = Path(output_dir)

    # Check if directory already exists
    if output_path.exists():
        messages.append(f"Warning: Directory already exists: {output_dir}")
        messages.append("Consider using a different name or removing the existing directory")
        return False, messages

    try:
        # Create main skill directory
        output_path.mkdir(parents=True, exist_ok=False)
        messages.append(f"✓ Created directory: {output_dir}")

        # Create SKILL.md with frontmatter
        skill_md_path = output_path / "SKILL.md"
        frontmatter = f"""---
name: {name}
description: {description}
---

# {name.replace('-', ' ').title()}

[Add your skill content here following the chosen template pattern]

## Usage

```bash
/{name} [arguments]
```

## Quick Start

[Add quick start guide]

## Implementation Guidelines

[Add implementation details]

## Examples

[Add examples]

## Notes

[Add any important notes]
"""
        skill_md_path.write_text(frontmatter)
        messages.append(f"✓ Created SKILL.md with validated frontmatter")

        # Create subdirectories based on template
        if template == 'scripts':
            scripts_dir = output_path / "scripts"
            scripts_dir.mkdir()
            messages.append(f"✓ Created scripts/ directory")

            # Create README in scripts directory
            (scripts_dir / "README.md").write_text("""# Scripts

Place your utility scripts here.

Scripts should:
- Solve problems rather than punt to the AI agent
- Have clear error messages
- Handle error conditions explicitly
- Include usage documentation
""")
            messages.append(f"✓ Created scripts/README.md")

        elif template == 'progressive':
            reference_dir = output_path / "reference"
            reference_dir.mkdir()
            messages.append(f"✓ Created reference/ directory")

            # Create README in reference directory
            (reference_dir / "README.md").write_text("""# Reference Files

Place detailed documentation here that will be loaded on-demand.

Guidelines:
- Keep files one level deep (no subdirectories)
- Use descriptive names (EXAMPLES.md, API_REFERENCE.md)
- Link from SKILL.md using: See [reference/FILENAME.md](reference/FILENAME.md)
- Each file should be focused on a specific domain or topic
""")
            messages.append(f"✓ Created reference/README.md")

        messages.append(f"\n✓ Successfully created skill structure")
        messages.append(f"✓ Template used: {template}")
        messages.append(f"\nNext steps:")
        messages.append(f"1. Edit {output_dir}/SKILL.md to add your skill content")
        messages.append(f"2. Follow the template pattern for your chosen type")
        messages.append(f"3. Test the skill with real usage scenarios")

        return True, messages

    except Exception as e:
        messages.append(f"✗ Error creating skill structure: {str(e)}")
        # Clean up partial creation
        if output_path.exists():
            try:
                shutil.rmtree(output_path)
                messages.append("✓ Cleaned up partial directory creation")
            except Exception as cleanup_error:
                messages.append(f"Warning: Could not clean up partial directory: {str(cleanup_error)}")
        return False, messages


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Create the AI agent skill directory structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python create_skill_structure.py \\
        --name "processing-pdfs" \\
        --description "Processes PDF files..." \\
        --template "basic" \\
        --output-dir ".agents/skills/processing-pdfs"

    python create_skill_structure.py \\
        --name "managing-databases" \\
        --description "Manages database migrations..." \\
        --template "scripts" \\
        --output-dir ".agents/skills/managing-databases"

Template Types:
    basic       - Text-only workflows, no scripts
    scripts     - Includes scripts/ directory for utilities
    progressive - Includes reference/ directory for detailed docs
        """
    )
    parser.add_argument('--name', required=True, help='Skill name (validated)')
    parser.add_argument('--description', required=True, help='Skill description (validated)')
    parser.add_argument(
        '--template',
        required=True,
        choices=AVAILABLE_TEMPLATES,
        help='Template type to use'
    )
    parser.add_argument('--output-dir', required=True, help='Output directory path')

    args = parser.parse_args()

    # Validate name
    print("Validating skill name...")
    name_valid, name_errors = validate_name(args.name)
    if not name_valid:
        print("✗ Invalid skill name:")
        for error in name_errors:
            print(f"  - {error}")
        sys.exit(1)
    print(f"✓ Name valid: {args.name}")

    # Validate description
    print("\nValidating skill description...")
    desc_valid, desc_errors, desc_warnings = validate_description(args.description)
    if not desc_valid:
        print("✗ Invalid skill description:")
        for error in desc_errors:
            print(f"  - {error}")
        sys.exit(1)
    print(f"✓ Description valid ({len(args.description)} characters)")
    if desc_warnings:
        print("Suggestions:")
        for warning in desc_warnings:
            print(f"  - {warning}")

    # Create structure
    print(f"\nCreating skill structure...")
    success, messages = create_skill_structure(
        args.name,
        args.description,
        args.template,
        args.output_dir
    )

    # Output results
    for message in messages:
        print(message)

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
