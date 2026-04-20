# omr

This directory contains the recreation for the Optical Music Recognition
experimentation performed. This contains another directory:

- `Models/` — Contains the simulation of the training of the models. Each model
inforamtion is stored in a different directory, containing:
    - `config`: yaml files for PyLaia.
    - `hyps`: resulting decoding of the test set.
    - `results`: resulting cer computed from the decoding of the test set.

A script `run_experiment.sh` is provided as an example of how PyLaia has been
used in the experimentation; specifically for the BPE 1-5 case. The 
`compute_cer.py` script is used for computing the CER results provided.
