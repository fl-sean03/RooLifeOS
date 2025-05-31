import pandas as pd
import matplotlib.pyplot as plt

def load_kpis():
    df = pd.read_csv('Module_G_Performance_Analytics_Review/Master_KPIs.csv')
    return df

def generate_bar_chart():
    df = load_kpis()
    ax = df.plot.bar(x='Metric', y=['Current', 'Target'])
    plt.title('KPI Progress')
    plt.xlabel('Metric')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig('Module_G_Performance_Analytics_Review/plots/kpi_progress.png')

if __name__ == "__main__":
    generate_bar_chart()