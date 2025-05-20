import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

class CrossCountryComparison:
    """Class for comparing solar metrics across countries."""
    
    def __init__(self, dfs, countries):
        self.dfs = dfs  # List of DataFrames
        self.countries = countries
    
    def boxplots(self):
        """Generate boxplots for GHI, DNI, DHI across countries."""
        combined = pd.concat([df.assign(Country=country) for df, country in zip(self.dfs, self.countries)])
        for metric in ['GHI', 'DNI', 'DHI']:
            plt.figure(figsize=(8, 6))
            sns.boxplot(x='Country', y=metric, data=combined)
            plt.title(f'{metric} Comparison Across Countries')
            plt.savefig(f'plots/{metric}_boxplot.png')
            plt.close()
    
    def summary_table(self):
        """Generate summary table for GHI, DNI, DHI."""
        summary = []
        for df, country in zip(self.dfs, self.countries):
            stats = {
                'Country': country,
                'GHI_mean': df['GHI'].mean(),
                'GHI_median': df['GHI'].median(),
                'GHI_std': df['GHI'].std(),
                'DNI_mean': df['DNI'].mean(),
                'DNI_median': df['DNI'].median(),
                'DNI_std': df['DNI'].std(),
                'DHI_mean': df['DHI'].mean(),
                'DHI_median': df['DHI'].median(),
                'DHI_std': df['DHI'].std()
            }
            summary.append(stats)
        summary_df = pd.DataFrame(summary)
        summary_df.to_csv('data/summary_table.csv', index=False)
        return summary_df
    
    def statistical_test(self):
        """Perform ANOVA test on GHI across countries."""
        ghi_values = [df['GHI'].dropna() for df in self.dfs]
        f_stat, p_value = f_oneway(*ghi_values)
        return {'f_stat': f_stat, 'p_value': p_value}
    
    def ranking_bar_chart(self):
        """Generate bar chart ranking countries by average GHI."""
        means = [df['GHI'].mean() for df in self.dfs]
        plt.figure(figsize=(8, 6))
        plt.bar(self.countries, means)
        plt.title('Average GHI by Country')
        plt.ylabel('Average GHI (W/m²)')
        plt.savefig('plots/ghi_ranking.png')
        plt.close()