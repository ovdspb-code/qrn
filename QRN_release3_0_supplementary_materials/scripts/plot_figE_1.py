#!/usr/bin/env python3
"""Plot Figure E-1 payoff criterion from figE_1_payoff.csv.

Produces figE_1_payoff.png in the current directory.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/figE_1_payoff.csv")

plt.figure()
plt.plot(df["N_active"], df["E_save_J"], label=r"$E_{save} \approx (N_{active}-1)E_{comm}$")

# Plot each E_tax line
tax_cols = [c for c in df.columns if c.startswith("E_tax_J_Ptax_")]
for c in sorted(tax_cols):
    plt.plot(df["N_active"], df[c], linestyle="--", label=c.replace("E_tax_J_Ptax_", r"$E_{tax}$ (")+ ")")

plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"Active subnet size $N_{active}$")
plt.ylabel("Energy per act (J)")
plt.title("QRN payoff criterion (Appendix E)")
plt.legend()
plt.tight_layout()
out = "figE_1_payoff.png"
plt.savefig(out, dpi=300)
print("Saved", out)
