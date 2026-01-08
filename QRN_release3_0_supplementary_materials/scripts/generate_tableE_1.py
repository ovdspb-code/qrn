#!/usr/bin/env python3
"""Generate Table E-1 (P_tax,max) as CSV.

Writes ../data/tableE_1_ptax_max.csv.
"""

import pandas as pd

E_comm = 2.5e-7  # J per event (illustrative value used in Appendix E)
N_list = [10, 50, 100, 500, 1000]
f_list = [0.1, 1, 10]  # Hz

rows = []
for N in N_list:
    for f in f_list:
        rows.append({
            "N_active": N,
            "f_fix_Hz": f,
            "P_tax_max_W": (N-1) * E_comm * f
        })

df = pd.DataFrame(rows)
out = "../data/tableE_1_ptax_max.csv"
df.to_csv(out, index=False)
print("Wrote", out)
