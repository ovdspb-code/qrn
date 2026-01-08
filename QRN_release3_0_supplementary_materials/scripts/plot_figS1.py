#!/usr/bin/env python3
"""Plot Figure S1 from figS1_horizon_convergence.csv.

Produces figS1_horizon_convergence.png in the current directory.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/figS1_horizon_convergence.csv")

for gamma in sorted(df["gamma"].unique()):
    sub = df[df["gamma"] == gamma].sort_values("horizon_T")
    plt.figure()
    plt.plot(sub["horizon_T"], sub["kappa_star_Psuccess"], marker="o", label=r"$\arg\max_\kappa P_{success}(T)$")
    plt.plot(sub["horizon_T"], sub["kappa_star_gap"], linestyle="--", label=r"$\arg\max_\kappa g$")
    plt.xscale("log")
    plt.xlabel("Horizon T (log scale)")
    plt.ylabel(r"Optimal dephasing $\kappa^*$")
    plt.title(f"gamma = {gamma:.1f} slice")
    plt.legend()
    plt.tight_layout()
    out = f"figS1_gamma_{gamma:.1f}.png"
    plt.savefig(out, dpi=300)
    print("Saved", out)
