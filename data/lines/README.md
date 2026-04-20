# lines

This directory contains data for the image lines used in the training of the OMR
models.

- `splits/` — Files with the list of lines used for train/test/val for the EIN 
dataset.
- `transcriptions/` — GT transcriptions provided for each split according to the
distribution in `splits/`, also the BPE encoded versions used in the experiments
are provided inside `bpe/`.
- `IMAGES/` — This folder should contain the images of the lines extracted from each
image of the real manuscripts. We do not own the rights for distributing the 
images, so this folder is empty. It has been created only for reproductibilty 
purposes.

Here, also the `.txt` symbol files for training the EIN models have been included.
