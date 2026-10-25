"""Check every post in _posts/ against the rules in WRITING-GUIDE.md and CLAUDE.md.

Standard library only, so it runs in CI without installing anything.
"""

import glob
import os
import re
import sys
from collections import defaultdict

REQUIRED_KEYS = ["layout", "categories", "title", "date", "series", "series_part", "description"]
FILENAME = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(-[a-z0-9]+)*\.md$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+0000$")
DASHES = ("—", "–")
LIMITS_HEADING = "## What it does not do"


def front_matter(text):
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip() != "":
        return None, None
    fields = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields, parts[2]


def first_paragraph(body):
    for block in body.strip().split("\n\n"):
        block = block.strip()
        if block and not block.startswith("#"):
            return block
    return ""


def check_file(path, errors):
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()

    match = FILENAME.match(name)
    if not match:
        errors.append(f"{name}: filename must be YYYY-MM-DD-short-kebab-title.md")
        return None

    fields, body = front_matter(text)
    if fields is None:
        errors.append(f"{name}: missing front matter")
        return None

    for key in REQUIRED_KEYS:
        if not fields.get(key):
            errors.append(f"{name}: front matter is missing '{key}'")

    if fields.get("layout") and fields["layout"] != "post":
        errors.append(f"{name}: layout must be 'post'")

    date = fields.get("date", "")
    if date and not DATE.match(date):
        errors.append(f"{name}: date must be 'YYYY-MM-DD HH:MM:SS +0000'")
    elif date and date[:10] != match.group(1):
        errors.append(f"{name}: date does not match the file name")

    if len(fields.get("title", "")) > 70:
        errors.append(f"{name}: title is longer than 70 characters")
    try:
        title_part = int(fields.get("series_part", ""))
    except ValueError:
        title_part = None
    if title_part is not None and not fields.get("title", "").startswith(f"Part {title_part}: "):
        errors.append(f"{name}: the title must start with 'Part {title_part}: '")
    if len(fields.get("description", "")) > 160:
        errors.append(f"{name}: description is longer than 160 characters")

    if any(d in text for d in DASHES):
        errors.append(f"{name}: contains an em dash or an en dash")

    if LIMITS_HEADING not in body:
        errors.append(f"{name}: missing the section '{LIMITS_HEADING}'")

    try:
        part = int(fields.get("series_part", ""))
    except ValueError:
        errors.append(f"{name}: series_part must be a whole number")
        return None

    if part > 1:
        previous = f"part {part - 1}"
        opening = first_paragraph(body).lower()
        if not re.search(rf"\b{previous}\b", opening):
            errors.append(f"{name}: the opening paragraph must refer back to {previous}")

    return fields.get("series"), part, name


def main():
    errors = []
    series = defaultdict(list)

    for path in sorted(glob.glob("_posts/*.md")):
        result = check_file(path, errors)
        if result:
            name_series, part, name = result
            series[name_series].append((part, name))

    for name_series, entries in series.items():
        numbers = sorted(part for part, _ in entries)
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append(
                f"series '{name_series}': part numbers must run 1 to {len(numbers)} with no gaps or repeats, found {numbers}"
            )

    if errors:
        print("Post checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    total = sum(len(entries) for entries in series.values())
    print(f"All {total} posts pass the checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
