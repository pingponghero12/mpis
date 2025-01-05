import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_max_load(df, d):
    nsum = df.groupby("n")["max_load"].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["n"], df["max_load"], marker="o", s=2, label="points", alpha=0.5)
    ax.scatter(nsum.index, nsum.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

    ax.set_title(f"Max Load Simulation Results for d={d}")
    ax.set_xlabel("n")
    ax.set_ylabel("Max Load")
    ax.legend()

    plt.savefig(f"images/max_load_d{d}.png")
    plt.close()

def plot_cmp(df):
    nsum = df.groupby("n")["cmp"].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["n"], df["cmp"], marker="o", s=2, label="points", alpha=0.5)
    ax.scatter(nsum.index, nsum.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

    ax.set_title(f"Cmp Simulation Results")
    ax.set_xlabel("n")
    ax.set_ylabel("Number of comparisions")
    ax.legend()

    plt.savefig(f"images/cmp.png")
    plt.close()

def plot_s(df):
    nsum = df.groupby("n")["s"].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["n"], df["s"], marker="o", s=2, label="points", alpha=0.5)
    ax.scatter(nsum.index, nsum.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

    ax.set_title(f"Shifting Simulation Results")
    ax.set_xlabel("n")
    ax.set_ylabel("Number of shifts")
    ax.legend()

    plt.savefig(f"images/s.png")
    plt.close()

def plot_ratios_ln(df, d):
    mean_values = df.groupby("n")["max_load"].mean()
    if d == 1:
        f_n = np.log(mean_values.index) / np.log(np.log(mean_values.index))
        title = "l_n^(1) / (ln(n)/ln(ln(n)))"
    elif d == 2:
        f_n = np.log(np.log(mean_values.index)) / np.log(2)
        title = "l_n^(2) / (ln(ln(n))/ln(2))"
    
    ratio = mean_values / f_n

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ratio.index, ratio.values, marker='o', linestyle='-', markersize=3)
    ax.set_title(title)
    ax.set_xlabel("n")
    ax.set_ylabel("Ratio")

    plt.savefig(f"images/ratio_d{d}.png")
    plt.close()

def plot_ex2_ratios(df):
    variables = ['cmp', 's']
    titles = {
        'cmp': ['cmp(n)/n', 'cmp(n)/n²'],
        's': ['s(n)/n', 's(n)/n²']
    }
    
    for var_name in variables:
        mean_values = df.groupby("n")[var_name].mean()
        
        fig = plt.figure(figsize=(10, 12))
        
        ratios = [
            mean_values / mean_values.index,
            mean_values / (mean_values.index**2)
        ]
        
        for i, (ratio, title) in enumerate(zip(ratios, titles[var_name]), 1):
            plt.subplot(len(ratios), 1, i)
            plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', markersize=3)
            plt.title(f"{var_name.upper()}: {title}")
            plt.xlabel("n")
            plt.ylabel("Ratio")
        
        plt.tight_layout()
        plt.savefig(f"images/{var_name}_ratios.png")
        plt.close()

def plot_ex3(df):
    p_values = df["p"].unique()
    
    for p in p_values:
        df_p = df[df["p"] == p]
        mean_values = df_p.groupby("n")["tn"].mean()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df_p["n"], df_p["tn"], marker="o", s=2, label="points", alpha=0.5)
        ax.scatter(mean_values.index, mean_values.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

        ax.set_title(f"Rounds Simulation Results for p={p}")
        ax.set_xlabel("n")
        ax.set_ylabel("Rounds")
        ax.legend()

        plt.savefig(f"images/rounds_p{p}.png")
        plt.close()

def plot_ex3_01(df):
    p_values = df["p"].unique()
    
    for p in p_values:
        df_p = df[df["p"] == p]
        mean_values = df_p.groupby("n")["tn"].mean()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df_p["n"], df_p["tn"], marker="o", s=2, label="points", alpha=0.5)
        ax.scatter(mean_values.index, mean_values.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

        ax.set_title(f"Rounds Simulation Results for p={p}")
        ax.set_xlabel("n")
        ax.set_ylabel("Rounds")
        ax.legend()

        plt.savefig(f"images/rounds_p{p}.png")
        plt.close()

def main():
    df_d1 = pd.read_csv("data/ex1_d1.csv")
    df_d2 = pd.read_csv("data/ex1_d2.csv")
    df_ex2 = pd.read_csv("data/ex2.csv")
    df_ex3 = pd.read_csv("data/ex3.csv")
    df_ex3_01 = pd.read_csv("data/ex3_01.csv")
    
    plot_max_load(df_d1, 1)
    plot_max_load(df_d2, 2)
    plot_ratios_ln(df_d1, 1)
    plot_ratios_ln(df_d2, 2)
    plot_ex2_ratios(df_ex2)
    plot_ex3(df_ex3)
    plot_cmp(df_ex2)
    plot_s(df_ex2)
    plot_ex3_01(df_ex3_01)

if __name__ == "__main__":
    main()
