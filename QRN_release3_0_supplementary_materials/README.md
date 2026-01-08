QRN Release 3.0 — Supplementary Materials (Data + Minimal Plotting Scripts)

This folder contains machine-readable supplementary datasets referenced in the QRN Release 3.0 manuscript,
specifically for:
• Appendix D: Figures S1 and S2 (finite-horizon κ* vs spectral-gap κ*; and robustness vs readout/sink rate η)
• Appendix E: Table E-1 and Figure E-1 (payoff / “energy advantage” checkpoints)

IMPORTANT SCOPE NOTE
The simulation code and figure-generation scripts for the main-text Figures 2–5 are already in the main
simulation repository (per the paper’s Data Availability statement). This supplement focuses on the additional
(non–Figures-2–5) numeric artefacts needed to reproduce Appendix D/E results without re-running the full simulations.

Directory structure
├── data/
│   ├── figS1_horizon_convergence.csv
│   ├── figS2_eta_robustness.csv
│   ├── tableE_1_ptax_max.csv
│   ├── figE_1_payoff.csv
│   └── appendixE_parameters.json
├── scripts/
│   ├── plot_figS1.py
│   ├── plot_figS2.py
│   ├── plot_figE_1.py
│   └── generate_tableE_1.py
└── requirements.txt

Data files
1) figS1_horizon_convergence.csv
   Columns: gamma, horizon_T, kappa_star_Psuccess, kappa_star_gap
   Meaning: For each horizon T (arbitrary units) and γ-slice, this table reports:
   • κ* that maximizes P_success(T) (finite-horizon optimum)
   • κ*_g that maximizes the Liouvillian gap g(γ,κ) (spectral diagnostic)
   This is the dataset behind Figure S1 (Appendix D).

2) figS2_eta_robustness.csv
   Columns: eta, kappa_star_gamma1, kappa_star_gamma2, kappa_star_gamma3, kappa_star_gamma4
   Meaning: κ*(γ,η) for γ ∈ {1,2,3,4} across η ∈ [0.05,2.0] (log scale).
   This is the dataset behind Figure S2 (Appendix D).

3) tableE_1_ptax_max.csv
   Columns: N_active, f_fix_Hz, P_tax_max_W
   Meaning: P_tax,max = (N_active−1)·E_comm·f_fix, using E_comm = 2.50e-07 J/event (illustrative).
   This reproduces Table E-1 (Appendix E).

4) figE_1_payoff.csv
   Columns: N_active, E_save_J, E_tax_J_Ptax_1e-06W, E_tax_J_Ptax_1e-05W
   Meaning:
   • E_save ≈ (N_active−1)·E_comm
   • E_tax = P_tax/f_fix + E_pre, with f_fix=1 Hz and E_pre=0 in the illustrative plot.
   This reproduces Figure E-1 (Appendix E).

Reproducing plots locally
1) Create a clean environment and install dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2) Run plotting scripts from scripts/:
   cd scripts
   python plot_figS1.py
   python plot_figS2.py
   python plot_figE_1.py

Outputs will be saved as PNG files in scripts/.

Provenance
• Appendix E tables/curves are computed directly from the explicit formulas in the manuscript.
• Figure S1 values follow the discrete κ*(T) values stated in Appendix D.
• Figure S2 values were digitized from the final Release 3.0 figure (η grid: 0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0)
  and are rounded to 3 decimals. If you prefer, regenerate κ*(γ,η) directly from the simulation codebase and overwrite
  figS2_eta_robustness.csv with the exact outputs.

Contact / integration
Recommended integration into the main repo:
  lindbladsim/
    supplementary_release3_0/
      (this folder)

Additional reproducibility artefact (recommended)
The toy-model potential uses random disorder ε_i ~ U[-0.5,0.5] and the manuscript notes that the realization is
“fixed by the script’s seed”. To make the numerical figures fully reproducible without relying on implicit RNG defaults,
it is recommended to publish:
  • the RNG seed used for Figures 2–5, and
  • the realized ε_i and V_i vectors.

Templates:
  • data/toy_model_potential_seed_TEMPLATE.csv
  • data/toy_model_config_TEMPLATE.json
