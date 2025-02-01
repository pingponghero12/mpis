import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import arcsine

df = pd.read_csv("data/out.csv")

for n in [100, 1000, 10000]:
    dfloc = df[df['n'] == n]
    data =dfloc['pn']

    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=np.linspace(0, 1, 21), density=True, alpha=0.5, edgecolor='black', label='Observed PDF (pn)')

    x = np.linspace(0.001, 0.999, 300)

    pdf_arcsine = 1 / (np.pi * np.sqrt(x * (1 - x)))
    plt.plot(x, pdf_arcsine, 'r-', lw=2, label='Arcsine PDF')

    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title(f"Histogram of pn values and Arcsine PDF for n={n}")
    plt.legend()

    plt.savefig(f"images/historgram_{n}.png")
    plt.show()
