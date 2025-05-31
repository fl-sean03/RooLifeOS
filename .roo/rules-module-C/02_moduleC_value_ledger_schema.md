# Module C: Strategic Value Ledger Schema

This document defines the Markdown table schema for `Strategic_Value_Ledger.md`.

## Value Ledger Table Template
The `Strategic_Value_Ledger.md` file must use the following header row:

```markdown
# Strategic Value Ledger

| Commitment | Milestone | Linked_Project                     | Value       | Date_Logged |
|------------|-----------|------------------------------------|-------------|-------------|
```

## Field Definitions
- `Commitment`: The name of the active commitment (e.g., PhD, LabLink, Opspawn).
- `Milestone`: A specific milestone achieved within that commitment.
- `Linked_Project`: A relative Markdown link to a Bridge Project in Module B (e.g., `[BP-001](../Module_B_Strategic_Pathways/Bridge_Project_Pipeline.md#BP-001)`). This links value extraction to strategic projects.
- `Value`: A description of the value extracted or created (e.g., "Published research paper", "Developed new feature", "Secured funding").
- `Date_Logged`: The date the value was logged (YYYY-MM-DD).

## Adding Rows
New value entries should be appended as new rows under the header, maintaining Markdown table formatting.

### Example Row
```markdown
| PhD Research | Chapter 1 Draft Complete | [BP-002](../Module_B_Strategic_Pathways/Bridge_Project_Pipeline.md#BP-002) | Draft of first thesis chapter | 2025-05-20 |