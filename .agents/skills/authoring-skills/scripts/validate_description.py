#!/usr/bin/env python3
"""Validate skill description against the AI agent requirements.

Usage:
    python validate_description.py "Description text..."
    python validate_description.py "Description text..." --json

Exit codes:
    0: Valid description
    1: Invalid description
"""

import re
import sys
import argparse
import json

# Validation constants
MAX_LENGTH = 1024
XML_CHARS = re.compile(r'[<>&]')

# POV patterns (first/second person indicators)
POV_PATTERNS = [
    (re.compile(r'\bI\b'), "I"),
    (re.compile(r'\byou\b', re.IGNORECASE), "you"),
    (re.compile(r'\byour\b', re.IGNORECASE), "your"),
    (re.compile(r'\bwe\b', re.IGNORECASE), "we"),
    (re.compile(r'\bour\b', re.IGNORECASE), "our"),
]

def validate_description(desc: str) -> tuple[bool, list[str], list[str]]:
    """Validate description against all rules.

    Args:
        desc: The skill description to validate

    Returns:
        Tuple of (is_valid, list_of_errors, list_of_warnings)

    Example:
        >>> validate_description("Processes PDF files...")
        (True, [], [])
        >>> validate_description("I help you process PDFs")
        (False, ["Description must be in third person..."], [])
    """
    errors = []
    warnings = []

    # Check if empty
    if not desc or not desc.strip():
        errors.append("Description cannot be empty")
        return False, errors, warnings

    # Check length
    if len(desc) > MAX_LENGTH:
        errors.append(
            f"Description exceeds maximum length of {MAX_LENGTH} characters "
            f"(got {len(desc)})"
        )

    # Check for XML characters
    if XML_CHARS.search(desc):
        errors.append("Cannot contain XML characters (<, >, &)")

    # Check POV (point of view)
    pov_found = []
    for pattern, word in POV_PATTERNS:
        if pattern.search(desc):
            pov_found.append(word)

    if pov_found:
        errors.append(
            f"Description must be in third person (found: {', '.join(pov_found)})"
        )
        errors.append(
            "Suggestion: Start with the skill's action "
            "(e.g., 'Processes...', 'Analyzes...', 'Manages...')"
        )

    # Check for "when to use" indicators
    when_indicators = ['use when', 'use for', ' when ', ' for ']
    has_when = any(indicator in desc.lower() for indicator in when_indicators)
    if not has_when:
        warnings.append(
            "Consider adding 'when to use' guidance "
            "(e.g., 'Use when...', 'Use for...')"
        )

    return len(errors) == 0, errors, warnings


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Validate the AI agent skill description',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validate_description.py "Processes PDF files..."          # Valid
    python validate_description.py "I help you process PDFs"         # Invalid: first person
    python validate_description.py "" --json                          # Invalid: empty

Description Requirements:
    - Maximum 1024 characters
    - Third person only (no "I", "you", "we")
    - Include what the skill does AND when to use it
    - Use specific key terms for discoverability
    - Be concrete, not vague

Good Example:
    "Extracts text and tables from PDF files, fills forms, merges documents.
    Use when working with PDF files or when the user mentions PDFs, forms, or
    document extraction."
        """
    )
    parser.add_argument('description', help='Skill description to validate')
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output in JSON format'
    )

    args = parser.parse_args()

    # Validate the description
    is_valid, errors, warnings = validate_description(args.description)

    # Output results
    if args.json:
        result = {
            'valid': is_valid,
            'length': len(args.description),
            'errors': errors,
            'warnings': warnings
        }
        print(json.dumps(result, indent=2))
    else:
        if is_valid:
            print(f"✓ Description valid ({len(args.description)} characters)")
            if warnings:
                print("\nSuggestions:")
                for warning in warnings:
                    print(f"  - {warning}")
        else:
            print("✗ Description invalid")
            for error in errors:
                print(f"  - {error}")
            if warnings:
                print("\nAdditional suggestions:")
                for warning in warnings:
                    print(f"  - {warning}")

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
