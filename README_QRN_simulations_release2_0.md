QRN Release 2.0 – Simulation README
=================================

This package contains the reference Python implementation used to generate the numerical figures in the QRN core manuscript (Release 2.0 draft). The code implements the GKSL/Lindblad toy model on a small graph (N=10 nodes + 1 sink) and produces:

• Figure 1: conceptual QRN architecture diagram (script-generated, non-simulation)
• Figure 2: targeting / cumulative sink capture P_success(t)
• Figure 3: expected potential (free-energy proxy) vs time
• Figure 4: finite-horizon efficiency landscape P_success(T; γ, κ)
• Figure 5: two-panel comparison of P_success(T; γ, κ) to the Liouvillian gap g(γ, κ)
• Appendix Figure S1: convergence of κ*(T)=argmax_κ P_success(T) to κ*_g=argmax_κ g as T increases

Files
-----

Main script:
  • qrn_article_simulations_release2_0_fixed.py

Generated figures (default names):
  • Fig1_QRN_Architecture_generated.png
  • Fig2_QRN_Targeting_generated.png
  • Fig3_QRN_ExpectedPotential_generated.png
  • Fig4_QRN_EfficiencyLandscape_generated.png
  • Fig5_QRN_Psuccess_vs_LiouvillianGap_generated.png
  • Appendix_TtoInf_kappaopt_convergence.png   (this is Figure S1 in the manuscript)

Saved data (optional, when using --save-data):
  • maps_Psuccess_gap.npz
      - gammas, kappas: parameter grid
      - P_map: P_success(T) on the grid
      - G_map: g(γ, κ) (Liouvillian gap) on the grid
      - N, eta, T, seed, V_pot: metadata for reproducibility
  • appendix_TtoInf_convergence.npz
      - T_list: list of horizons
      - kappas: κ grid
      - results: per-slice arrays for κ*(T) and κ*_g

Requirements
------------

• Python 3.10+ recommended
• numpy
• scipy
• matplotlib
• networkx  (only for Figure 1 diagram)

A minimal install is:

  pip install numpy scipy matplotlib networkx

Reproducing all figures
-----------------------

Run the full pipeline:

  python qrn_article_simulations_release2_0_fixed.py --mode all --outdir qrn_outputs --save-data

Selective generation
--------------------

Use --mode to generate specific groups:

• --mode fig1      Generates Figure 1 only
• --mode fig23     Generates Figures 2–3 only
• --mode fig45     Generates Figures 4–5 only
• --mode fig4      Generates Figure 4 only
• --mode fig5      Generates Figure 5 only
• --mode figX      Alias for fig5 (kept for backwards compatibility)
• --mode appendix  Generates Appendix Figure S1 only

Example:

  python qrn_article_simulations_release2_0_fixed.py --mode fig5 --outdir qrn_outputs

Reproducibility notes
---------------------

• The diagonal potential V_pot is generated from a fixed random seed defined in the script (QRNParams.seed). Changing the seed will change the landscape.
• For N=10, the Liouvillian acts on an 11×11 density matrix, i.e., it is a 121×121 superoperator after vectorization.
• For larger N, computing the full spectrum becomes expensive; the code is structured to use sparse operators and iterative eigensolvers for the rightmost part of the spectrum.

Data availability / citation
----------------------------

The public repository and archived snapshot referenced in the manuscript:

• GitHub: https://github.com/noisethewhite/lindbladsim
• Zenodo DOI: 10.5281/zenodo.18133404
