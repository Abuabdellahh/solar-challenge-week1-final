import matplotlib.pyplot as plt
import seaborn as sns

class SolarVisualizer:
    def __init__(self, df):
        self.df = df
        
    def plot_time_series(self, column, title):
        """Plot time series data"""
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='Timestamp', y=column, data=self.df)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt
    
    def plot_correlation_heatmap(self, columns):
        """Plot correlation heatmap for selected columns"""
        plt.figure(figsize=(10, 8))
        corr = self.df[columns].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Feature Correlation Heatmap')
        return plt
    
    def plot_boxplots(self, metric, countries):
        """Generate comparative boxplots"""
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='country', y=metric, data=countries)
        plt.title(f'Comparative {metric} Analysis')
        plt.xticks(rotation=45)
        return plt