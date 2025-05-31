# Module F: CSV Schema Guidelines

This document defines the schema for CSV files within Module F, specifically for `Energy_Log.csv`.

## `Energy_Log.csv` Header
The `Energy_Log.csv` file must use the following header row:

```csv
Date,Sleep_Hours,Energy_Peak_Start,Energy_Peak_End,Nutrition_Score,Exercise_Minutes,Notes
```

## Example Data Row
When adding a new row, ensure it follows this format:

```csv
2025-05-31,7.5,09:00,12:00,8,60,"Felt productive after morning workout"
```

## Field Definitions
- `Date`: The date of the log entry (YYYY-MM-DD).
- `Sleep_Hours`: Number of hours slept.
- `Energy_Peak_Start`: Start time of your peak energy period (HH:MM).
- `Energy_Peak_End`: End time of your peak energy period (HH:MM).
- `Nutrition_Score`: A self-assessed score for your nutrition that day (e.g., 1-10).
- `Exercise_Minutes`: Number of minutes exercised.
- `Notes`: Any additional notes or observations about your energy, health, or focus.