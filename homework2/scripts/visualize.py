import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_random_variable(df, var_name):
    nsum = df.groupby("n")[var_name].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["n"], df[var_name], marker="o", s=2, label="points", alpha=0.5)
    ax.scatter(nsum.index, nsum.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

    ax.set_title(f"{var_name.upper()} Simulation Results")
    ax.set_xlabel("n")
    ax.set_ylabel(f"{var_name.upper()} Value")
    ax.legend()

    plt.savefig(f"images/{var_name}_simulation.png")
    plt.close()

def plot_ratios(df):
    variables = ['bn', 'un', 'cn', 'dn', 'diff']
    
    for var_name in variables:
        mean_values = df.groupby("n")[var_name].mean()
        
        fig = plt.figure(figsize=(10, 12))
        
        if var_name == 'bn':
            ratios = [
                mean_values / mean_values.index,
                mean_values / np.sqrt(mean_values.index)
            ]
            titles = ['b(n)/n', 'b(n)/√n']
        
        elif var_name == 'un':
            ratios = [mean_values / mean_values.index]
            titles = ['u(n)/n']
        
        elif var_name == 'cn':
            ratios = [
                mean_values / mean_values.index,
                mean_values / (mean_values.index * np.log(mean_values.index)),
                mean_values / (mean_values.index**2)
            ]
            titles = ['c(n)/n', 'c(n)/(n*ln(n))', 'c(n)/n²']
        
        elif var_name == 'dn':
            ratios = [
                mean_values / mean_values.index,
                mean_values / (mean_values.index * np.log(mean_values.index)),
                mean_values / (mean_values.index**2)
            ]
            titles = ['d(n)/n', 'd(n)/(n*ln(n))', 'd(n)/n²']
        
        elif var_name == 'diff':
            ratios = [
                mean_values / mean_values.index,
                mean_values / (mean_values.index * np.log(mean_values.index)),
                mean_values / (mean_values.index * np.log(np.log(mean_values.index)))
            ]
            titles = ['(d(n)-c(n))/n', '(d(n)-c(n))/(n*ln(n))', '(d(n)-c(n))/(n*ln(ln(n)))']
        
        for i, (ratio, title) in enumerate(zip(ratios, titles), 1):
            plt.subplot(len(ratios), 1, i)
            plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', markersize=3)
            plt.title(f"{var_name.upper()}: {title}")
            plt.xlabel("n")
            plt.ylabel("Ratio")
        
        plt.tight_layout()
        plt.savefig(f"images/{var_name}_ratios.png")
        plt.close()

def main():
    df = pd.read_csv("data.csv")
    
    variables = ['bn', 'un', 'cn', 'dn', 'diff']
    
    for var in variables:
        plot_random_variable(df, var)
    
    plot_ratios(df)

if __name__ == "__main__":
    main()
