import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

df = pd.read_csv('data/asdf100.csv')

N_VALUES = sorted(df['n'].unique())  # [5, 10, ..., 30]

n_groups = [N_VALUES[i:i + 4] for i in range(0, len(N_VALUES), 4)]

for group_idx, n_group in enumerate(n_groups):
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))
    fig.suptitle('Empirical Distribution of Random Walks\nCompared to Normal Distribution', fontsize=16)
    
    for idx, n in enumerate(n_group):
        row = idx // 2
        col = idx % 2
        
        n_data = df[df['n'] == n].sort_values('value')
        
        axs[row, col].bar(n_data['value'], n_data['probability'], 
                         alpha=0.6, label='Empirical', color='blue')
        
        x = np.linspace(min(n_data['value']), max(n_data['value']), 100)
        theoretical_normal = norm.cdf(x, loc=0, scale=np.sqrt(n))
        axs[row, col].plot(x, theoretical_normal, 'r-', 
                          label='Theoretical Normal', linewidth=2)
        
        axs[row, col].set_title(f'n = {n}')
        axs[row, col].set_xlabel('Value')
        axs[row, col].set_ylabel('Cumulative Probability')
        axs[row, col].legend()
        axs[row, col].grid(True)

        if idx == len(n_group) - 1:
            for j in range(idx + 1, 4):
                axs[j // 2, j % 2].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f'images/random_walks_distribution_{group_idx + 1}.png', 
                dpi=300, bbox_inches='tight')
    plt.close()

plt.figure(figsize=(12, 8))
for n in N_VALUES:
    n_data = df[df['n'] == n].sort_values('value')
    plt.plot(n_data['value'], n_data['probability'], 
             label=f'n = {n}', alpha=0.7)

plt.title('Comparison of CDFs for Different n Values')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)

plt.tight_layout()
#plt.savefig('images/random_walks_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
