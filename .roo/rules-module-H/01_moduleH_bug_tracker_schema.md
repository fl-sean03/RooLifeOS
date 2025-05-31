# Module H: Bug Tracker Schema

This document defines the Markdown table schema for `Bug_Tracker.md` within Module H.

## Bug Tracker Table Template
The `Bug_Tracker.md` file must use the following header row:

```markdown
# Bug Tracker

| ID      | Description                     | Status   | Priority | Date_Logged | Notes            |
| ------- | ------------------------------- | -------- | -------- | ----------- | ---------------- |
```

## Example Data Row
When adding a new bug entry, ensure it follows this format:

```markdown
| BUG-001 | YAML syntax error in Module B | Open    | High    | 2025-05-31  | Needs quick fix    |
```

## Field Definitions
- `ID`: Unique identifier for the bug (e.g., BUG-001).
- `Description`: A brief description of the bug.
- `Status`: Current status of the bug (e.g., Open, In Progress, Resolved, Closed).
- `Priority`: The urgency of fixing the bug (e.g., High, Medium, Low).
- `Date_Logged`: The date the bug was logged (YYYY-MM-DD).
- `Notes`: Any additional notes, steps to reproduce, or workarounds.