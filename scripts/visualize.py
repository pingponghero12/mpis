import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy

def print_fig(file_name, title_name, true_value, four):
    df = pd.read_csv(f"data/{file_name}")
    df["int"] = df["int"] * four

    nsum = df.groupby("n")["int"].mean()

    fig, ax = plt.subplots()
    ax.scatter(df["n"], df["int"], marker="o", s=2, label="points")
    ax.plot([50, 5000], [true_value, true_value], color="tab:green", linewidth=3, label="true value")
    ax.scatter(nsum.index, nsum.values, marker="o", s=10, label="mean", color="tab:red", zorder=3)

    ax.set_title(title_name)
    ax.set_xlabel("n")
    ax.set_ylabel("Integral value")


    ax.legend()

    plt.savefig(f"images/{title_name}.png")

    plt.show()

def exp_fitting():
    df1 = pd.read_csv("data/ex1-50.csv")
    df2 = pd.read_csv("data/ex2-50.csv")
    df3 = pd.read_csv("data/ex3-50.csv")

    max1 = df1.groupby("n")["int"].max()
    max1 = np.log(max1)
    max2 = df2.groupby("n")["int"].max()
    max2 = np.log(max2)
    max3 = df3.groupby("n")["int"].max()
    max3 = np.log(max3)

    def expf(x, a, b):
        return a + b*np.log(x)

    exp_fit1 = scipy.optimize.curve_fit(expf, max1.index, max1.values)
    exp_fit2 = scipy.optimize.curve_fit(expf, max2.index, max2.values)
    exp_fit3 = scipy.optimize.curve_fit(expf, max3.index, max3.values)

    x = np.linspace(50, 5000, num=1000)
    y1 = expf(x, exp_fit1[0][0], exp_fit1[0][1])
    y2 = expf(x, exp_fit2[0][0], exp_fit2[0][1])
    y3 = expf(x, exp_fit3[0][0], exp_fit3[0][1])

    correlation1 = np.corrcoef(max1.values, expf(max1.index, exp_fit1[0][0], exp_fit1[0][1]))[0,1]
    correlation2 = np.corrcoef(max2.values, expf(max2.index, exp_fit2[0][0], exp_fit2[0][1]))[0,1]
    correlation3 = np.corrcoef(max3.values, expf(max3.index, exp_fit3[0][0], exp_fit3[0][1]))[0,1]
    print(f"Correlations: {correlation1}, {correlation2}, {correlation3}")
    print(f"Mean: {(correlation1+correlation2+correlation3)/3}")
    
    fig, ax = plt.subplots(3, 1, figsize=(5, 9), sharex=True, sharey=False)
    ax[0].scatter(max1.index, max1.values, s=3, color="tab:blue")
    ax[0].plot(x, y1, color="tab:red")
    ax[1].scatter(max2.index, max2.values, s=3, color="tab:blue")
    ax[1].plot(x, y2, color="tab:red")
    ax[2].scatter(max3.index, max3.values, s=3, color="tab:blue")
    ax[2].plot(x, y3, color="red")
    plt.savefig("skibidi.png")
    plt.show()

def exp_fitting_test():
    df1 = pd.read_csv("data/ex1-50.csv")
    df2 = pd.read_csv("data/ex2-50.csv")
    df3 = pd.read_csv("data/ex3-50.csv")

    max1 = df1.groupby("n")["int"].max()
    max2 = df2.groupby("n")["int"].max()
    max3 = df3.groupby("n")["int"].max()

    def expf(x, a, b):
        return a * np.exp(b * x)

    # Fit the exponential function
    exp_fit = scipy.optimize.curve_fit(
        expf, 
        x_scaled, 
        max1.values, 
        p0=[max1.values.mean(), -0.1], 
        bounds=([0, -np.inf], [np.inf, np.inf])
    )

    # Create smooth x values for plotting
    x1 = np.linspace(max1.index.min(), max1.index.max(), num=1000)
    # Scale these x values the same way
    x1_scaled = (x1 - max1.index.min()) / (max1.index.max() - max1.index.min())
    # Calculate y values using scaled x
    y1 = exp_fit[0][0] * np.exp(exp_fit[0][1] * x1_scaled)
    
    # Plot both the original data and the fitted curve
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(max1.index, max1.values, 'o', label='Data points')
    ax.plot(x1, y1, 'r-', label='Fitted curve')
    
    ax.set_xlabel('n')
    ax.set_ylabel('Maximum interval')
    ax.set_title('Exponential Fit of Maximum Intervals')
    ax.legend()
    
    plt.grid(True)
    plt.show()

    return exp_fit
    

print_fig("ex1-5.csv", "ex1-5", 12, 1)
print_fig("ex1-50.csv", "ex1-50", 12, 1)

print_fig("ex2-5.csv", "ex2-5", 2, 1)
print_fig("ex2-50.csv", "ex2-50", 2, 1)

print_fig("ex3-5.csv", "ex3-5", 0.2, 1)
print_fig("ex3-50.csv", "ex3-50", 0.2, 1)

print_fig("ex4-5.csv", "ex4-5", np.pi, 4)
print_fig("ex4-50.csv", "ex4-50", np.pi, 4)

exp_fitting()
exp_fitting_test()
