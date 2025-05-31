# Module G: CSV Schema Guidelines

This document defines the schema for CSV files within Module G, specifically for `Master_KPIs.csv`.

## `Master_KPIs.csv` Header
The `Master_KPIs.csv` file must use the following header row:

```csv
Metric,Current,Target,Unit,Last_Updated
```

## Example Data Row
When adding a new row, ensure it follows this format:

```csv
Monthly Revenue,10000,12000,USD,2025-05-31
```

## Field Definitions
- `Metric`: The name of the Key Performance Indicator (e.g., "Monthly Revenue", "Website Visitors", "Conversion Rate").
- `Current`: The current value of the metric.
- `Target`: The desired target value for the metric.
- `Unit`: The unit of measurement for the metric (e.g., USD, %, #).
- `Last_Updated`: The date the metric was last updated (YYYY-MM-DD).