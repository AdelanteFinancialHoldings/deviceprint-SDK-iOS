#!/usr/bin/env python3
"""Validate YAML frontmatter in SKILL.md file.

Usage:
    python validate_frontmatter.py /path/to/SKILL.md
    python validate_frontmatter.py /path/to/SKILL.md --json

Exit codes:
    0: Valid frontmatter
    1: Invalid frontmatter
"""

import re
import sys
import argparse
import json
from pathlib import Path

# Import validation functions from other scripts
try:
    from validate_name import validate_name
    from validate_description import validate_description
except ImportError:
    # Fallback if imports fail - use simplified validation
    def validate_name(name):
        if not name or len(name) > 64:
            return False, ["Invalid name"]
        return True, []

    def validate_description(desc):
        if not desc or len(desc) > 1024:
            return False, ["Invalid description"], []
        return True, [], []


def extract_frontmatter(content: str) -> tuple[dict, list[str]]:
    """Extract YAML frontmatter from SKILL.md content.

    Args:
        content: The full file content

    Returns:
        Tuple of (frontmatter_dict, errors)
    """
    errors = []

    # Match YAML frontmatter (between --- delimiters)
    pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL | re.MULTILINE)
    match = pattern.match(content)

    if not match:
        errors.append("No YAML frontmatter found (must start with --- and end with ---)")
        return {}, errors

    frontmatter_text = match.group(1)

    # Parse simple YAML (name and description fields)
    frontmatter = {}

    name_match = re.search(r'^name:\s*(.+)$', frontmatter_text, re.MULTILINE)
    if name_match:
        frontmatter['name'] = name_match.group(1).strip()
    else:
        errors.append("Missing 'name' field in frontmatter")

    desc_match = re.search(r'^description:\s*(.+)$', frontmatter_text, re.MULTILINE)
    if desc_match:
        frontmatter['description'] = desc_match.group(1).strip()
    else:
        errors.append("Missing 'description' field in frontmatter")

    return frontmatter, errors


def validate_frontmatter_file(filepath: str) -> tuple[bool, dict]:
    """Validate frontmatter in a SKILL.md file.

    Args:
        filepath: Path to SKILL.md file

    Returns:
        Tuple of (is_valid, results_dict)
    """
    results = {
        'file': filepath,
        'frontmatter': {},
        'errors': [],
        'warnings': []
    }

    # Read file
    try:
        content = Path(filepath).read_text()
    except FileNotFoundError:
        results['errors'].append(f"File not found: {filepath}")
        return False, results
    except Exception as e:
        results['errors'].append(f"Error reading file: {str(e)}")
        return False, results

    # Extract frontmatter
    frontmatter, extraction_errors = extract_frontmatter(content)
    results['frontmatter'] = frontmatter
    results['errors'].extend(extraction_errors)

    if extraction_errors:
        return False, results

    # Validate name field
    if 'name' in frontmatter:
        name_valid, name_errors = validate_name(frontmatter['name'])
        if not name_valid:
            results['errors'].extend([f"Name: {err}" for err in name_errors])

    # Validate description field
    if 'description' in frontmatter:
        desc_valid, desc_errors, desc_warnings = validate_description(frontmatter['description'])
        if not desc_valid:
            results['errors'].extend([f"Description: {err}" for err in desc_errors])
        results['warnings'].extend([f"Description: {warn}" for warn in desc_warnings])

    is_valid = len(results['errors']) == 0
    return is_valid, results


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Validate YAML frontmatter in SKILL.md file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validate_frontmatter.py skill/SKILL.md
    python validate_frontmatter.py skill/SKILL.md --json

This script validates both the structure of the frontmatter and the
content of the name and description fields according to the AI agent
skill requirements.
        """
    )
    parser.add_argument('filepath', help='Path to SKILL.md file')
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output in JSON format'
    )

    args = parser.parse_args()

    # Validate frontmatter
    is_valid, results = validate_frontmatter_file(args.filepath)

    # Output results
    if args.json:
        output = {
            'valid': is_valid,
            **results
        }
        print(json.dumps(output, indent=2))
    else:
        if is_valid:
            print(f"✓ Frontmatter valid in: {args.filepath}")
            print(f"  Name: {results['frontmatter'].get('name', 'N/A')}")
            print(f"  Description: {results['frontmatter'].get('description', 'N/A')[:60]}...")
            if results['warnings']:
                print("\nSuggestions:")
                for warning in results['warnings']:
                    print(f"  - {warning}")
        else:
            print(f"✗ Frontmatter invalid in: {args.filepath}")
            for error in results['errors']:
                print(f"  - {error}")
            if results['warnings']:
                print("\nAdditional suggestions:")
                for warning in results['warnings']:
                    print(f"  - {warning}")

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
