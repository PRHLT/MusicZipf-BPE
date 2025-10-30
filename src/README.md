# Source Code

This directory contains the source code used to perform analyses and generate 
results presented in the paper.

The code is organized into submodules according to their purpose.


| Folder | Description |
|--------|-------------|
| `bpe/` | Code for training a **Byte Pair Encoding (BPE)** configuration to generate a vocabulary of musical words. |
| `fit/` | Scripts for fitting empirical data to the **ZMS (Zipf-Mandelbrot-Simon) model**, producing the estimated parameters used in the paper. |
| `metrics/` | Functions to compare empirical data to the ZMS estimations. Computes the evaluation metrics **R²** and **Kolmogorov-Smirnov (K-S) distance**, as described in the paper. |
| `plot/` | Code to generate **Zipf curves** for a given vocabulary and ZMS estimation, used to create figures shown in the paper. |
