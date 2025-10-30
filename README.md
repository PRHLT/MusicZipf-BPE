# Byte Pair Encoding for Musical Data

<!-- [![DOI](...)](...) -->

This repository contains the code and data accompanying the paper:

> **Plainchant Music Modeling through Zipf's Law**,
> Aitana Menárguez-Box, Enrique Vidal and Alejandro H. Toselli 2025
> 
> [to be completed]

---

## Repository Structure

- `data/` → Raw and processed datasets.
- `src/` → Source code for preprocessing, BPE and visualization.
- `notebooks/` → Jupyter notebooks demonstrating example usage and reproducing results.
- `results/` → Audio samples generated through the experiments described in the 
paper and resulting data for the execution of the Jupyter notebooks inside 
`notebooks/`.
- `environment.yml` → Conda environment file for reproducing the software setup.

Each subdirectory includes its own `README.md` with additional details.

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/PRHLT/MusicZipf-BPE.git
cd MusicZipf-BPE
```

### 2. Setup the environment
Option A — Using Conda:
```bash
conda env create -f environment.yml
conda activate bpe-env
```

Option B — Using pip and virtualenv:
```bash
python3 -m venv bpe-env
source bpe-env/bin/activate
pip install -r requirements.txt
```

### 3. Install required system tools
The following system tools are required to run the scripts:
- gnuplot
- awk
- sort
- nl
- cp
- rm

These are typically preinstalled on Linux and macOS systems.
If not, install them using your package manager:
```bash
# Ubuntu / Debian
sudo apt update
sudo apt install gnuplot gawk coreutils

# macOS (with Homebrew)
brew install gnuplot gawk coreutils
```

For Windows users, it’s recommended to use WSL ([Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/)) to ensure these commands are available.

### 4. Test your installation
Once the environment is ready, you can test that everything works by running:
```bash
python3 src/bpe/train_bpe.py --help
```

This command should display the list of available options for training a BPE
vocabulary and confirm that the environment is correctly set up.

---

## Citation
If you use this code or data, please cite:

```bibtex
[to be completed]
```

---

## Data Sources and Acknowledgements

This repository includes data derived from historical plainchant music sheet manuscripts.
Three collections constitute the datasets used in this work, all consisting of plainchant sheet music images:

- **Einsiedeln (CH-E 611)** — a 14th-century antiphoner from the monastery of Einsiedeln, Switzerland.  
- **Salzinnes (CDN-Hsmu M2149.L4)** — a Cistercian antiphoner from the Abbey of Salzinnes (Belgium), completed between 1554 and 1555. Provided by the **Patrick Power Library**, St. Mary’s University (Canada).  
- **Vorau-253 (Cod-253)** — from the library of Vorau Abbey, Austria, dated to approximately 1450. Provided by the **ACDH-CH Institute** of the Austrian Academy of Sciences.

*Raw* transcriptions and music-lyrics alignments for the **Einsiedeln** and **Salzinnes** manuscripts were obtained from the **Cantus Ultimus Database** ([Cantus Database](https://cantusdatabase.org)):

> **Recommended citation:**  
> *Cantus Database.* Directed by Debra Lacoste (2011–present), Terence Bailey (1997–2010), and Ruth Steiner (1987–1996); developed for the web by Jan Koláček (2011–2023), McGill University Distributed Digital Music Archives & Libraries Lab – DDMAL (2023–present); and funded through the *Digital Analysis of Chant Transmission* project at Dalhousie University, Halifax, Nova Scotia, Canada (SSHRC 895-2023-1002), directed by Jennifer Bain, [https://cantusdatabase.org](https://cantusdatabase.org). Accessed [insert your access date].

The transcription for **Vorau-253**, without alignment information, was produced in our laboratories.

We gratefully acknowledge the institutions and databases that made these materials available.  
If you use this repository, please also cite the original sources accordingly.

---

## License
All materials in this repository (code and data) are released under the 
[Creative Commons Attribution–NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

You are free to use, modify, and share this work **for non-commercial purposes**, 
provided you give appropriate credit by citing the paper above.

Commercial use is not permitted.
If you wish to use this code or data for commercial purposes, please contact the authors.
