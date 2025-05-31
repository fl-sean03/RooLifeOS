# Module G: Dashboard Script Template

This document provides a template for `Dashboard_Scripts.py` within Module G. This script will read `Master_KPIs.csv` and generate basic charts.

## Python Script Template
```python
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_kpis():
    """Loads KPI data from Master_KPIs.csv."""
    df = pd.read_csv('Module_G_Performance_Analytics_Review/Master_KPIs.csv')
    return df

def generate_bar_chart():
    """Generates a bar chart of current vs. target KPIs and saves it to the plots/ folder."""
    df = load_kpis()

    # Ensure the plots directory exists
    plots_dir = 'Module_G_Performance_Analytics_Review/plots'
    os.makedirs(plots_dir, exist_ok=True)

    ax = df.plot.bar(x='Metric', y=['Current', 'Target'], figsize=(10, 6))
    plt.title('KPI Progress: Current vs. Target')
    plt.xlabel('Metric')
    plt.ylabel('Value')
    plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'kpi_progress.png'))
    plt.close() # Close the plot to free up memory

if __name__ == "__main__":
    generate_bar_chart()
```

## Usage
- This script can be executed to generate a `kpi_progress.png` image in the `plots/` directory.
- You can extend this script to include more sophisticated data analysis, different chart types, or integration with other data sources.