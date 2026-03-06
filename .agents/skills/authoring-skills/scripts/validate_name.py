#!/usr/bin/env python3
"""Validate skill name against the AI agent requirements.

Usage:
    python validate_name.py "skill-name"
    python validate_name.py "skill-name" --json

Exit codes:
    0: Valid name
    1: Invalid name
"""

import re
import sys
import argparse
import json

# Validation constants
RESERVED_WORDS = ['anthropic', 'claude']
MAX_LENGTH = 64
VALID_PATTERN = re.compile(r'^[a-z0-9-]+$')
XML_CHARS = re.compile(r'[<>&]')

def validate_name(name: str) -> tuple[bool, list[str]]:
    """Validate skill name against all rules.

    Args:
        name: The skill name to validate

    Returns:
        Tuple of (is_valid, list_of_errors)

    Example:
        >>> validate_name("processing-pdfs")
        (True, [])
        >>> validate_name("ProcessingPDFs")
        (False, ["Must use lowercase letters, numbers, and hyphens only"])
        >>> validate_name("pdf-processing")
        (False, ["Name must start with a gerund..."])
    """
    errors = []

    # Check if empty
    if not name or not name.strip():
        errors.append("Name cannot be empty")
        return False, errors

    # Check length
    if len(name) > MAX_LENGTH:
        errors.append(
            f"Name exceeds maximum length of {MAX_LENGTH} characters "
            f"(got {len(name)})"
        )

    # Check valid characters pattern
    if not VALID_PATTERN.match(name):
        invalid_chars = set(c for c in name if not re.match(r'[a-z0-9-]', c))
        char_list = ', '.join(f"'{c}'" for c in sorted(invalid_chars))
        errors.append(
            f"Must use lowercase letters, numbers, and hyphens only. "
            f"Found invalid characters: {char_list}"
        )

    # Check for XML characters
    if XML_CHARS.search(name):
        errors.append("Cannot contain XML characters (<, >, &)")

    # Check for start/end hyphens (spec requirement)
    if name.startswith('-'):
        errors.append("Name must not start with a hyphen")
    if name.endswith('-'):
        errors.append("Name must not end with a hyphen")

    # Check for consecutive hyphens (spec requirement)
    if '--' in name:
        errors.append("Name must not contain consecutive hyphens (--)")

    # Check for reserved words
    for reserved in RESERVED_WORDS:
        if reserved in name.lower():
            errors.append(f'Cannot use reserved word: "{reserved}"')

    # Check gerund form: first segment must end with "ing" (min 4 chars)
    if VALID_PATTERN.match(name):
        first_segment = name.split('-')[0]
        if len(first_segment) < 4 or not first_segment.endswith('ing'):
            errors.append(
                "Name must start with a gerund (verb ending in -ing). "
                "Example: 'processing-pdfs', not 'pdf-processing'"
            )

    return len(errors) == 0, errors


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Validate the AI agent skill name',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validate_name.py "processing-pdfs"     # Valid name
    python validate_name.py "ProcessingPDFs"      # Invalid: uppercase
    python validate_name.py "claude-helper"       # Invalid: reserved word
    python validate_name.py "test" --json         # JSON output

Naming Rules:
    - Gerund form required: "processing-pdfs", "analyzing-data"
    - Rejected: "pdf-processing", "data-analysis" (not gerund form)
    - Avoid: "helper", "utils", "tools" (too vague)
        """
    )
    parser.add_argument('name', help='Skill name to validate')
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output in JSON format'
    )

    args = parser.parse_args()

    # Validate the name
    is_valid, errors = validate_name(args.name)

    # Output results
    if args.json:
        result = {
            'valid': is_valid,
            'name': args.name,
            'errors': errors
        }
        print(json.dumps(result, indent=2))
    else:
        if is_valid:
            print(f"✓ Name valid: {args.name}")
        else:
            print(f"✗ Name invalid: {args.name}")
            for error in errors:
                print(f"  - {error}")
            print("\nSuggestions:")
            print("  - Use lowercase letters, numbers, and hyphens only")
            print("  - Must start with a gerund: processing-pdfs, analyzing-data")
            print("  - Keep it under 64 characters")
            print("  - Avoid reserved words: anthropic, claude")

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
