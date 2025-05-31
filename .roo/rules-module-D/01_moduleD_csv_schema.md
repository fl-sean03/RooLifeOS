# Module D: CSV Schema Guidelines

This document defines the schema for CSV files within Module D, specifically for `Master_Learning_List.csv`.

## `Master_Learning_List.csv` Header
The `Master_Learning_List.csv` file must use the following header row:

```csv
Topic,Category,Priority,Status,Date_Added,Estimated_Hours,Linked_ILP,Notes
```

## Example Data Row
When adding a new row, ensure it follows this format:

```csv
Example Skill,General,High,Planned,2025-01-15,20,ILP_Example_Skill.md,"Notes about skill"
```

## Field Definitions
- `Topic`: The subject or skill to be learned.
- `Category`: The broad category of the topic (e.g., Programming, Business, Personal Development).
- `Priority`: The importance of learning this topic (e.g., High, Medium, Low).
- `Status`: Current status of learning (e.g., Planned, In Progress, Completed, On Hold).
- `Date_Added`: The date the topic was added to the list (YYYY-MM-DD).
- `Estimated_Hours`: Estimated hours required to achieve proficiency.
- `Linked_ILP`: A link to an Individual Learning Plan (ILP) Markdown file, if applicable (e.g., `ILP_Example_Skill.md`).
- `Notes`: Any additional notes or comments.