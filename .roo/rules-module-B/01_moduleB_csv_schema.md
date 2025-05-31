# Module B: CSV Schema Guidelines

This document defines the schema for CSV files within Module B, specifically for `Knowledge_Skill_Gaps.csv`.

## `Knowledge_Skill_Gaps.csv` Header
The `Knowledge_Skill_Gaps.csv` file must use the following header row:

```csv
Gap_ID,Skill,Description,Current_Level,Target_Level,Priority,Status,Date_Identified
```

## Example Data Row
When adding a new row, ensure it follows this format:

```csv
SKG-001,Example Skill,Description...,Beginner,Advanced,High,Planned,2025-01-01
```

## Field Definitions
- `Gap_ID`: Unique identifier for the skill gap (e.g., SKG-001).
- `Skill`: The name of the skill.
- `Description`: A brief description of the skill gap.
- `Current_Level`: Your current proficiency level (e.g., Beginner, Intermediate, Advanced).
- `Target_Level`: Your desired proficiency level.
- `Priority`: The importance of addressing this gap (e.g., High, Medium, Low).
- `Status`: Current status of addressing the gap (e.g., Planned, In Progress, Completed, On Hold).
- `Date_Identified`: The date the skill gap was identified (YYYY-MM-DD).