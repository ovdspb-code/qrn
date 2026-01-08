#!/usr/bin/env python3
"""Plot Figure S2 from figS2_eta_robustness.csv.

Produces figS2_eta_robustness.png in the current directory.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/figS2_eta_robustness.csv")

plt.figure()
plt.plot(df["eta"], df["kappa_star_gamma1"], marker="o", label="gamma=1.0")
plt.plot(df["eta"], df["kappa_star_gamma2"], marker="s", label="gamma=2.0")
plt.plot(df["eta"], df["kappa_star_gamma3"], marker="D", label="gamma=3.0")
plt.plot(df["eta"], df["kappa_star_gamma4"], marker="^", label="gamma=4.0")

plt.xscale("log")
plt.xlabel("Readout / sink rate eta (log scale)")
plt.ylabel(r"Optimal dephasing $\kappa^*$")
plt.title("Optimal dephasing increases with readout rate")
plt.legend()
plt.tight_layout()
out = "figS2_eta_robustness.png"
plt.savefig(out, dpi=300)
print("Saved", out)
